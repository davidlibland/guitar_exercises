"""
This module contains domains available in SDTM format.
"""
import demo.core as types_core
import demo.v18.variables as types_var

_DM_TABLE = [
    (types_var.STUDYID, types_core.CoreStatus.Required),
    (types_var.DOMAIN, types_core.CoreStatus.Required),
    (types_var.USUBJID, types_core.CoreStatus.Required),
    (types_var.SUBJID, types_core.CoreStatus.Required),
    (types_var.RFSTDTC, types_core.CoreStatus.Expected),
    (types_var.RFENDTC, types_core.CoreStatus.Expected),
    (types_var.RFXSTDTC, types_core.CoreStatus.Expected),
    (types_var.RFXENDTC, types_core.CoreStatus.Expected),
    (types_var.RFICDTC, types_core.CoreStatus.Expected),
    (types_var.RFPENDTC, types_core.CoreStatus.Expected),
    (types_var.DTHDTC, types_core.CoreStatus.Expected),
    (types_var.DTHFL, types_core.CoreStatus.Expected),
    (types_var.SITEID, types_core.CoreStatus.Required),
    (types_var.INVID, types_core.CoreStatus.Permissible),
    (types_var.INVNAM, types_core.CoreStatus.Permissible),
    (types_var.BRTHDTC, types_core.CoreStatus.Permissible),
    (types_var.AGE, types_core.CoreStatus.Expected),
    (types_var.AGEU, types_core.CoreStatus.Expected),
    (types_var.SEX, types_core.CoreStatus.Required),
    (types_var.RACE, types_core.CoreStatus.Expected),
    (types_var.ETHNIC, types_core.CoreStatus.Permissible),
    (types_var.ARMCD, types_core.CoreStatus.Required),
    (types_var.ARM, types_core.CoreStatus.Required),
    (types_var.ACTARMCD, types_core.CoreStatus.Required),
    (types_var.ACTARM, types_core.CoreStatus.Required),
    (types_var.COUNTRY, types_core.CoreStatus.Required),
    (types_var.DMDTC, types_core.CoreStatus.Permissible),
    (types_var.DMDY, types_core.CoreStatus.Permissible),
]

DM_SPEC = types_core.DomainSpec(
    name="DM",
    label="Demographics",
    variables=[x[0] for x in _DM_TABLE],
    core_flags=[x[1] for x in _DM_TABLE],
    description="""
    The Demographics domain includes a set of essential standard variables that describe each subject in a clinical study. It is the parent domain for all other
observations for human clinical subjects.
    """,
)
"""The DM domain spec."""
