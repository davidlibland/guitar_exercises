"""
This module defines the subset of variables that are allowed in SDTM v1.8
"""
from textwrap import dedent

import demo.core as types_core

STUDYID = types_core.VariableSpec(
    name="STUDYID",
    label="Study Identifier",
    type=types_core.VariableType.Identifier,
    subtype=None,
    datatype=str,
    description="Unique identifier for a study.",
)

DOMAIN = types_core.VariableSpec(
    name="DOMAIN",
    label="Domain Abbreviation",
    type=types_core.VariableType.Identifier,
    subtype=None,
    datatype=str,
    description="Two-character abbreviation for the domain.",
)

USUBJID = types_core.VariableSpec(
    name="USUBJID",
    label="Unique Subject Identifier",
    type=types_core.VariableType.Identifier,
    subtype=None,
    datatype=str,
    description=dedent(
        """
    Identifier used to uniquely identify a subject across all studies for all 
    applications or submissions involving the product. This must be a unique number, 
    and could be a compound identifier formed by concatenating STUDYID-SITEID-SUBJID."""
    ),
)

SUBJID = types_core.VariableSpec(
    name="SUBJID",
    label="Subject Identifier for the Study",
    type=types_core.VariableType.Topic,
    subtype=None,
    datatype=str,
    description=dedent(
        """
    Subject identifier, which must be unique within the study. Often the ID of the subject
    as recorded on a CRF."""
    ),
)

RFSTDTC = types_core.VariableSpec(
    name="RFSTDTC",
    label="Subject Reference Start Date/Time",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Reference Start Date/time for the subject in ISO 8601 character format. Usually
    equivalent to date/time when subject was first exposed to study treatment. Required 
    for all randomized subjects; will be null for all subjects who did not meet the 
    milestone the date requires, such as screen failures or unassigned subjects."""
    ),
)

RFENDTC = types_core.VariableSpec(
    name="RFENDTC",
    label="Subject Reference End Date/Time",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Reference End Date/time for the subject in ISO 8601 character format. Usually
    equivalent to the date/time when subject was determined to have ended the trial, and
    often equivalent to date/time of last exposure to study treatment. Required for all
    randomized subjects; null for screen failures or unassigned subjects."""
    ),
)

RFXSTDTC = types_core.VariableSpec(
    name="RFXSTDTC",
    label="Date/Time of First Study Treatment",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    First date of exposure to any protocol-specified treatment or therapy, equal to the
    earliest value of EXSTDTC."""
    ),
)

RFXENDTC = types_core.VariableSpec(
    name="RFXENDTC",
    label="Date/Time of Last Study Treatment",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Last date of exposure to any protocol-specified treatment or therapy, equal to the 
    latest value of EXENDTC (or the latest value of EXSTDTC if EXENDTC was not collected
    or is missing)."""
    ),
)

RFICDTC = types_core.VariableSpec(
    name="RFICDTC",
    label="Date/Time of Informed Consent",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Date/time of informed consent in ISO 8601 character format. This will be the same as
    the date of informed consent in the Disposition domain, if that protocol milestone is
    documented. Would be null only in studies not collecting the date of informed consent.
    """
    ),
)

RFPENDTC = types_core.VariableSpec(
    name="RFPENDTC",
    label="Date/Time of End of Participation",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Date/time when subject ended participation or follow-up in a trial, as defined in the
    protocol, in ISO 8601 character format. Should correspond to the last known date of
    contact. Examples include completion date, withdrawal date, last follow-up, date
    recorded for lost to follow up, or death date."""
    ),
)

DTHDTC = types_core.VariableSpec(
    name="DTHDTC",
    label="Date/Time of Death",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Date/time of death for any subject who died, in ISO 8601 format. Should represent the
    date/time that is captured in the clinical-trial database."""
    ),
)

DTHFL = types_core.VariableSpec(
    name="DTHFL",
    label="Subject Death Flag",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Indicates the subject died. Should be Y or null. Should be populated even when the
    death date is unknown."""
    ),
)

SITEID = types_core.VariableSpec(
    name="SITEID",
    label="Study Site Identifier",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description="Unique identifier for a site within a study.",
)

INVID = types_core.VariableSpec(
    name="INVID",
    label="Investigator Identifier",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    An identifier to describe the Investigator for the study. May be used in addition to
    SITEID. Not needed if SITEID is equivalent to INVID.
    """
    ),
)

INVNAM = types_core.VariableSpec(
    name="INVNAM",
    label="Identifier Name",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Synonym,
    datatype=str,
    description="Name of the investigator for a site.",
)

BRTHDTC = types_core.VariableSpec(
    name="BRTHDTC",
    label="Date/Time of Birth",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description="Date/time of birth of the subject.",
)

AGE = types_core.VariableSpec(
    name="AGE",
    label="Age",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=float,
    description=dedent(
        """Age expressed in AGEU. May be derived from RFSTDTC and BRTHDTC,
    but BRTHDTC may not be available in all cases (due to subject privacy concerns)."""
    ),
)

AGEU = types_core.VariableSpec(
    name="AGEU",
    label="Age Units",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Variable,
    datatype=str,
    description="Units associated with AGE.",
)

SEX = types_core.VariableSpec(
    name="SEX",
    label="Sex",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description="Sex of the subject.",
)

RACE = types_core.VariableSpec(
    name="RACE",
    label="Race",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Race of the subject. Sponsors should refer to “Collection of Race and Ethnicity Data 
    in Clinical Trials” (FDA, September 2005) for guidance regarding the collection of
    race (http://www.fda.gov/RegulatoryInformation/Guidances/ucm126340.htm) See
    Assumption below regarding RACE."""
    ),
)

ETHNIC = types_core.VariableSpec(
    name="ETHNIC",
    label="Ethnicity",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    The ethnicity of the subject. Sponsors should refer to “Collection of Race and 
    Ethnicity Data in Clinical Trials” (FDA, September 2005) for guidance regarding the 
    collection of ethnicity
    (http://www.fda.gov/RegulatoryInformation/Guidances/ucm126340.htm)."""
    ),
)

ARMCD = types_core.VariableSpec(
    name="ARMCD",
    label="Planned Arm Code",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    ARMCD is limited to 20 characters and does not have special character restrictions.
    Qualifier The maximum length of ARMCD is longer than for other “short” variables to
    accommodate the kind of values that are likely to be needed for crossover trials. For
    example, if ARMCD values for a seven-period crossover were constructed using two-
    character abbreviations for each treatment and separating hyphens, the length of
    ARMCD values would be 20."""
    ),
)

ARM = types_core.VariableSpec(
    name="ARM",
    label="Description of Planned Arm",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description="Name of the Arm to which the subject was assigned.",
)

ACTARMCD = types_core.VariableSpec(
    name="ACTARMCD",
    label="Actual Arm Code",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Code of actual Arm. When an Arm is not planned (not in Trial Arms), ACTARMCD
    will be UNPLAN. Randomized subjects who were not treated will be given a value of
    NOTTRT. Values should be “SCRNFAIL” for screen failures and “NOTASSGN” for
    subjects not assigned to treatment. Restricted to values in Trial Arms in all other 
    cases. ACTARMCD is limited to 20 characters and does not have special character
    restrictions. The maximum length of ACTARMCD is longer than for other short
    variables to accommodate the kind of values that are likely to be needed for crossover
    trials.
    """
    ),
)

ACTARM = types_core.VariableSpec(
    name="ACTARM",
    label="Description of Actual Arm",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Synonym,
    datatype=str,
    description=dedent(
        """
    Description of actual Arm. When an Arm is not planned (not in Trial Arms), ACTARM
    will be “Unplanned Treatment”. Randomized subjects who were not treated will be
    given a value of “Not Treated”. Values should be “Screen Failure” for screen failures
    and “Not Assigned” for subjects not assigned to treatment. Restricted to values in 
    Trial Arms in all other cases.
    """
    ),
)

COUNTRY = types_core.VariableSpec(
    name="COUNTRY",
    label="Country",
    type=types_core.VariableType.Qualifier,
    subtype=types_core.QualifierSubType.Record,
    datatype=str,
    description=dedent(
        """
    Country of the investigational site in which the subject participated in the trial.
    """
    ),
)

DMDTC = types_core.VariableSpec(
    name="DMDTC",
    label="Date/Time of Collection",
    type=types_core.VariableType.Timing,
    subtype=None,
    datatype=str,
    description="Date/time of demographic data collection.",
)

DMDY = types_core.VariableSpec(
    name="DMDY",
    label="Study Day of Collection",
    type=types_core.VariableType.Timing,
    subtype=None,
    datatype=int,
    description="Study day of collection measured as integer days.",
)
