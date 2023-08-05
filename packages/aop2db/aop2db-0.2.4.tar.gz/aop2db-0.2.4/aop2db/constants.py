"""String definitions."""

from . import LATEST_XML_VERSION

DATABASE = "DATABASE"

ID = "@id"
AOP_ID = "aop_id"
APPLICABILITY = "applicability"
TAXONOMY = "taxonomy"
EVIDENCE = "evidence"
SEX = "sex"
LIFESTAGE = "life-stage"
LAST_MODIFIED = "last_modified"
LM_TIMESTAMP = "last-modification-timestamp"
CREATION = "creation"
CREATION_TIMESTAMP = "creation-timestamp"
REFERENCES = "references"

# API
TAX_ID_LOOKUP = "https://rest.ensembl.org/taxonomy/id/{}?content-type=application/json"

# AOP Download
AOP_XML_DOWNLOAD = f"https://aopwiki.org/downloads/aop-wiki-xml-{LATEST_XML_VERSION}.gz"
