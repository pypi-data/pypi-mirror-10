"""
Protein-Ligand Interaction Profiler - Analyze and visualize protein-ligand interactions in PDB files.
detection.py - Detect non-covalent interactions.
Copyright 2014 Sebastian Salentin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Python standard library
import itertools

# Own modules
from supplemental import *
import config


##################################################
# FUNCTIONS FOR DETECTION OF SPECIFIC INTERACTIONS
##################################################

def hydrophobic_interactions(atom_set_a, atom_set_b):
    """Detection of hydrophobic pliprofiler between atom_set_a (binding site) and atom_set_b (ligand).
    Definition: All pairs of qualified carbon atoms within a distance of HYDROPH_DIST_MAX
    """
    data = namedtuple('hydroph_interaction', 'bsatom ligatom distance restype resnr reschain')
    pairings = []
    for a, b in itertools.product(atom_set_a.atoms, atom_set_b.atoms):
        e = euclidean3d(a.coords, b.coords)
        if e < config.HYDROPH_DIST_MAX:
            contact = data(bsatom=a, ligatom=b, distance=e, restype=whichrestype(a),
                           resnr=whichresnumber(a), reschain=whichchain(a))
            pairings.append(contact)
    return pairings


def hbonds(acceptors, donor_pairs, protisdon, typ):
    """Detection of hydrogen bonds between sets of acceptors and donor pairs.
    Definition: All pairs of hydrogen bond acceptor and donors with
    donor hydrogens and acceptor showing a distance within HBOND DIST MIN and HBOND DIST MAX
    and donor angles above HBOND_DON_ANGLE_MIN
    """
    data = namedtuple('hbond', 'a d h distance_ah distance_ad angle type protisdon resnr restype reschain sidechain atype dtype')
    pairings = []
    for acc, don in itertools.product(acceptors, donor_pairs):
        if typ == 'strong':  # Regular (strong) hydrogen bonds
            dist_ah = euclidean3d(acc.a.coords, don.h.coords)
            dist_ad = euclidean3d(acc.a.coords, don.d.coords)
            if dist_ad < config.HBOND_DIST_MAX:
                vec1, vec2 = vector(don.h.coords, don.d.coords), vector(don.h.coords, acc.a.coords)
                v = vecangle(vec1, vec2)
                if v > config.HBOND_DON_ANGLE_MIN:
                    restype = whichrestype(don.d) if protisdon else whichrestype(acc.a)
                    reschain = whichchain(don.d) if protisdon else whichchain(acc.a)
                    protatom = don.d.OBAtom if protisdon else acc.a.OBAtom
                    is_sidechain_hbond = protatom.GetResidue().GetAtomProperty(protatom, 8)  # Check if sidechain atom
                    resnr = whichresnumber(don.d)if protisdon else whichresnumber(acc.a)
                    contact = data(a=acc.a, d=don.d, h=don.h, distance_ah=dist_ah, distance_ad=dist_ad, angle=v,
                                   type=typ, protisdon=protisdon, resnr=resnr, restype=restype, reschain=reschain,
                                   sidechain=is_sidechain_hbond, atype=acc.a.type, dtype=don.d.type)
                    pairings.append(contact)
    return pairings


def pistacking(rings_bs, rings_lig):
    """Return all pi-stackings between the given aromatic ring systems in receptor and ligand."""
    data = namedtuple('pistack', 'proteinring ligandring distance angle offset type restype resnr reschain')
    pairings = []
    for r, l in itertools.product(rings_bs, rings_lig):
        # DISTANCE AND RING ANGLE CALCULATION
        d = euclidean3d(r.center, l.center)
        b = vecangle(r.normal, l.normal)
        a = min(b, 180-b if not 180-b < 0 else b)  # Smallest of two angles, depending on direction of normal

        # RING CENTER OFFSET CALCULATION (project each ring center into the other ring)
        proj1 = projection(l.normal, l.center, r.center)
        proj2 = projection(r.normal, r.center, l.center)
        offset = min(euclidean3d(proj1, l.center), euclidean3d(proj2, r.center))

        # RECEPTOR DATA
        resnr, restype, reschain = whichresnumber(r.atoms[0]), whichrestype(r.atoms[0]), whichchain(r.atoms[0])

        # SELECTION BY DISTANCE, ANGLE AND OFFSET
        if d < config.PISTACK_DIST_MAX:
            if 0 < a < config.PISTACK_ANG_DEV and offset < config.PISTACK_OFFSET_MAX:
                contact = data(proteinring=r, ligandring=l, distance=d, angle=a, offset=offset,
                               type='P', resnr=resnr, restype=restype, reschain=reschain)
                pairings.append(contact)
            if 90-config.PISTACK_ANG_DEV < a < 90+config.PISTACK_ANG_DEV and offset < config.PISTACK_OFFSET_MAX:
                contact = data(proteinring=r, ligandring=l, distance=d, angle=a, offset=offset,
                               type='T', resnr=resnr, restype=restype, reschain=reschain)
                pairings.append(contact)

    return pairings


def pication(rings, pos_charged, protcharged):
    """Return all pi-Cation interaction between aromatic rings and positively charged groups.
    For tertiary and quaternary amines, check also the angle between the ring and the nitrogen.
    """
    data = namedtuple('pication', 'ring charge distance offset type restype resnr reschain protcharged')
    pairings = []
    if not len(rings) == 0 and not len(pos_charged) == 0:
        for ring in rings:
            c = ring.center
            for p in pos_charged:
                d = euclidean3d(c, p.center)
                # Project the center of charge into the ring and measure distance to ring center
                proj = projection(ring.normal, ring.center, p.center)
                offset = euclidean3d(proj, ring.center)
                if d < config.PICATION_DIST_MAX and offset < config.PISTACK_OFFSET_MAX:
                    if type(p).__name__ == 'lcharge' and p.fgroup == 'tertamine':
                        # Special case here if the ligand has a tertiary amine, check an additional angle
                        # Otherwise, we might have have a pi-cation interaction 'through' the ligand
                        n_atoms = [a_neighbor for a_neighbor in OBAtomAtomIter(p.atoms[0].OBAtom)]
                        n_atoms_coords = [(a.x(), a.y(), a.z()) for a in n_atoms]
                        amine_normal = np.cross(vector(n_atoms_coords[0], n_atoms_coords[1]),
                                                vector(n_atoms_coords[2], n_atoms_coords[0]))
                        b = vecangle(ring.normal, amine_normal)
                        # Smallest of two angles, depending on direction of normal
                        a = min(b, 180-b if not 180-b < 0 else b)
                        if not a > 30.0:
                            resnr, restype = whichresnumber(ring.atoms[0]), whichrestype(ring.atoms[0])
                            reschain = whichchain(ring.atoms[0])
                            contact = data(ring=ring, charge=p, distance=d, offset=offset, type='regular',
                                           restype=restype, resnr=resnr, reschain=reschain, protcharged=protcharged)
                            pairings.append(contact)
                        break
                    resnr = whichresnumber(p.atoms[0]) if protcharged else whichresnumber(ring.atoms[0])
                    restype = whichrestype(p.atoms[0]) if protcharged else whichrestype(ring.atoms[0])
                    reschain = whichchain(p.atoms[0]) if protcharged else whichchain(ring.atoms[0])
                    contact = data(ring=ring, charge=p, distance=d, offset=offset, type='regular', restype=restype,
                                   resnr=resnr, reschain=reschain, protcharged=protcharged)
                    pairings.append(contact)
    return pairings


def saltbridge(poscenter, negcenter, protispos):
    """Detect all salt bridges (pliprofiler between centers of positive and negative charge)"""
    data = namedtuple('saltbridge', 'positive negative distance protispos resnr restype reschain')
    pairings = []
    for pc, nc in itertools.product(poscenter, negcenter):
        if euclidean3d(pc.center, nc.center) < config.SALTBRIDGE_DIST_MAX:
            resnr = pc.resnr if protispos else nc.resnr
            restype = pc.restype if protispos else nc.restype
            reschain = pc.reschain if protispos else nc.reschain
            contact = data(positive=pc, negative=nc, distance=euclidean3d(pc.center, nc.center), protispos=protispos,
                           resnr=resnr, restype=restype, reschain=reschain)
            pairings.append(contact)
    return pairings


def halogen(acceptor, donor):
    """Detect all halogen bonds of the type Y-O...X-C"""
    data = namedtuple('halogenbond', 'acc don distance don_angle acc_angle restype resnr reschain donortype acctype')
    pairings = []
    for acc, don in itertools.product(acceptor, donor):
        dist = euclidean3d(acc.o.coords, don.x.coords)
        if dist < config.HALOGEN_DIST_MAX:
            vec1, vec2 = vector(acc.o.coords, acc.y.coords), vector(acc.o.coords, don.x.coords)
            vec3, vec4 = vector(don.x.coords, acc.o.coords), vector(don.x.coords, don.c.coords)
            acc_angle, don_angle = vecangle(vec1, vec2), vecangle(vec3, vec4)
            if config.HALOGEN_ACC_ANGLE-config.HALOGEN_ANGLE_DEV < acc_angle < config.HALOGEN_ACC_ANGLE+config.HALOGEN_ANGLE_DEV:
                if config.HALOGEN_DON_ANGLE-config.HALOGEN_ANGLE_DEV < don_angle < config.HALOGEN_DON_ANGLE+config.HALOGEN_ANGLE_DEV:
                    contact = data(acc=acc, don=don, distance=dist, don_angle=don_angle, acc_angle=acc_angle,
                                   restype=whichrestype(acc.o), resnr=whichresnumber(acc.o),
                                   reschain=whichchain(acc.o), donortype=don.x.OBAtom.GetType(), acctype=acc.o.type)
                    pairings.append(contact)
    return pairings


def water_bridges(bs_hba, lig_hba, bs_hbd, lig_hbd, water):
    """Find water-bridged hydrogen bonds between ligand and protein. For now only considers bridged of first degree."""
    data = namedtuple('waterbridge', 'a atype d dtype h water distance_aw distance_dw d_angle w_angle type resnr restype reschain protisdon')
    pairings = []
    # First find all acceptor-water pairs with distance within d
    # and all donor-water pairs with distance within d and angle greater theta
    lig_aw, prot_aw, lig_dw, prot_hw = [], [], [], []
    for w in water:
        for acc1 in lig_hba:
            dist = euclidean3d(acc1.a.coords, w.coords)
            if config.WATER_BRIDGE_MINDIST <= dist <= config.WATER_BRIDGE_MAXDIST:
                lig_aw.append((acc1, w, dist))
        for acc2 in bs_hba:
            dist = euclidean3d(acc2.a.coords, w.coords)
            if config.WATER_BRIDGE_MINDIST <= dist <= config.WATER_BRIDGE_MAXDIST:
                prot_aw.append((acc2, w, dist))
        for don1 in lig_hbd:
            dist = euclidean3d(don1.d.coords, w.coords)
            d_angle = vecangle(vector(don1.h.coords, don1.d.coords), vector(don1.h.coords, w.coords))
            if config.WATER_BRIDGE_MINDIST <= dist <= config.WATER_BRIDGE_MAXDIST and d_angle > config.WATER_BRIDGE_THETA_MIN:
                lig_dw.append((don1, w, dist, d_angle))
        for don2 in bs_hbd:
            dist = euclidean3d(don2.d.coords, w.coords)
            d_angle = vecangle(vector(don2.h.coords, don2.d.coords), vector(don2.h.coords, w.coords))
            if config.WATER_BRIDGE_MINDIST <= dist <= config.WATER_BRIDGE_MAXDIST and d_angle > config.WATER_BRIDGE_THETA_MIN:
                prot_hw.append((don2, w, dist, d_angle))

    for l, p in itertools.product(lig_aw, prot_hw):
        acc, wl, distance_aw = l
        don, wd, distance_dw, d_angle = p
        if wl == wd:  # Same water molecule and angle within omega
            w_angle = vecangle(vector(acc.a.coords, wl.coords), vector(wl.coords, don.h.coords))
            if config.WATER_BRIDGE_OMEGA_MIN < w_angle < config.WATER_BRIDGE_OMEGA_MAX:
                contact = data(a=acc.a, atype=acc.a.type, d=don.d, dtype=don.d.type, h=don.h, water=wl,
                               distance_aw=distance_aw, distance_dw=distance_dw,
                               d_angle=d_angle, w_angle=w_angle, type='first_deg', resnr=whichresnumber(don.d),
                               restype=whichrestype(don.d), reschain=whichchain(don.d), protisdon=True)
                pairings.append(contact)
    for p, l in itertools.product(prot_aw, lig_dw):
        acc, wl, distance_aw = p
        don, wd, distance_dw, d_angle = l
        if wl == wd:  # Same water molecule and angle within omega
            w_angle = vecangle(vector(acc.a.coords, wl.coords), vector(wl.coords, don.h.coords))
            if config.WATER_BRIDGE_OMEGA_MIN < w_angle < config.WATER_BRIDGE_OMEGA_MAX:
                contact = data(a=acc.a, atype=acc.a.type, d=don.d, dtype=don.d.type, h=don.h, water=wl,
                               distance_aw=distance_aw, distance_dw=distance_dw, d_angle=d_angle, w_angle=w_angle,
                               type='first_deg', resnr=whichresnumber(acc.a),
                               restype=whichrestype(acc.a), reschain=whichchain(acc.a), protisdon=False)
                pairings.append(contact)
    return pairings
