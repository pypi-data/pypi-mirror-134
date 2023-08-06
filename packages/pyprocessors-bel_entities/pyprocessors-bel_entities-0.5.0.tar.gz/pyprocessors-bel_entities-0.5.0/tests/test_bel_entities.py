import json
from pathlib import Path

import pytest
from pymultirole_plugins.v1.schema import Document
from pyprocessors_bel_entities.bel_entities import BELEntitiesProcessor, BELEntitiesParameters


# Arrange
@pytest.fixture
def original_doc():
    testdir = Path(__file__).parent
    source = Path(testdir, 'data/response_1639473035420.json')
    with source.open("r") as fin:
        doc = json.load(fin)
        original_doc = Document(**doc)
        return original_doc


def test_bel_entities(original_doc):
    doc = original_doc.copy(deep=True)
    processor = BELEntitiesProcessor()
    parameters = BELEntitiesParameters(kill_label='killed')
    docs = processor.process([doc], parameters)
    doc0: Document = docs[0]
    assert len(doc0.annotations) < len(original_doc.annotations)
    pass
