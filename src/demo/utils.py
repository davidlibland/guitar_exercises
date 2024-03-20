"""
This module contains the type of for demographics tables.
"""
from typing import Optional

import numpy as np

import demo.core as types_core
import demo.v18.domains as v18_domains


# pylint: disable=too-many-locals,too-many-statements
def random_demographics_table(
    nsubjects: int, generator: Optional[np.random.Generator] = None
) -> types_core.DomainTable:
    """
    Generate a random valid demographics table.

    Args:
        nsubjects: number of subjects to generate data for.
        generator: the random number generator instance to use for generation

    Returns:
        result: the generated data table
    """
    if generator is None:
        # create a new generator
        generator = np.random.default_rng()

    data = {}

    # generate studyid
    studyid = generator.integers(low=1, high=5000, size=1, dtype=int).repeat(
        nsubjects
    )

    # domain is DM
    domain = np.empty(nsubjects, dtype=object)
    domain[:] = "DM"

    # site id
    sites = generator.permutation(500)[:5]
    siteid = generator.choice(
        sites, p=[0.3, 0.3, 0.2, 0.1, 0.1], size=nsubjects, replace=True
    )
    country = np.empty_like(siteid, dtype=object)
    country[siteid == sites[0]] = "USA"
    country[siteid == sites[1]] = "USA"
    country[siteid == sites[2]] = "DEU"
    country[siteid == sites[3]] = "SWE"
    country[siteid == sites[4]] = "FRA"

    # subject id
    subject_id = generator.permutation(int(1.2 * nsubjects))[:nsubjects]

    # unique subject id
    unique_subject_id = [
        f"{x}-{y}-{z}" for x, y, z in zip(studyid, siteid, subject_id)
    ]

    # age
    age = np.floor(generator.normal(loc=60, scale=10, size=nsubjects))
    # ageu
    ageu = np.empty(nsubjects, dtype=object)
    ageu[:] = "YEARS"

    # sex
    sex_code = generator.binomial(n=1, p=0.67, size=nsubjects)
    sex = ["F" if x == 1 else 0 for x in sex_code]

    # race
    race = generator.choice(
        [
            "WHITE",
            "BLACK OR AFRICAN AMERICAN",
            "ASIAN",
            "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER",
            "OTHER",
        ],
        p=[0.7, 0.15, 0.05, 0.05, 0.05],
        replace=True,
        size=nsubjects,
    )

    # ethnic
    ethnic = generator.choice(
        ["", "NOT HISPANIC OR LATINO", "HISPANIC OR LATINO"],
        replace=True,
        p=[0.6, 0.3, 0.1],
        size=nsubjects,
    )

    # Arm
    arm_code = generator.choice(3, p=[0.4, 0.5, 0.1], size=nsubjects)
    armcd = np.empty(nsubjects, dtype=object)
    armcd[arm_code == 0] = "ST0"
    armcd[arm_code == 1] = "ST1"
    armcd[arm_code == 2] = "ST2"

    arm = np.empty(nsubjects, dtype=object)
    arm[arm_code == 0] = "Placebo"
    arm[arm_code == 1] = "ST1 Treatment 1"
    arm[arm_code == 2] = "ST2 Treatment 2"

    actarmcd = armcd
    actarm = arm

    data["STUDYID"] = studyid.tolist()
    data["DOMAIN"] = domain.tolist()
    data["USUBJID"] = unique_subject_id
    data["SUBJID"] = subject_id.tolist()
    data["RFSTDTC"] = None
    data["RFENDTC"] = None
    data["DTHDTC"] = None
    data["DTHFL"] = None
    data["SITEID"] = siteid.tolist()
    data["INVID"] = None
    data["INVNAM"] = None
    data["BRTHDTC"] = None
    data["AGE"] = age.tolist()
    data["AGEU"] = ageu.tolist()
    data["SEX"] = sex
    data["RACE"] = race.tolist()
    data["ETHNIC"] = ethnic.tolist()
    data["ARMCD"] = armcd.tolist()
    data["ARM"] = arm.tolist()
    data["ACTARMCD"] = actarmcd.tolist()
    data["ACTARM"] = actarm.tolist()
    data["COUNTRY"] = country.tolist()
    data["DMDTC"] = None
    data["DMDY"] = None

    return types_core.DomainTable(meta=v18_domains.DM_SPEC, data=data)
