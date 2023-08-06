import logging

from dkist_processing_common.tasks.mixin.metadata_store import MetadataStoreMixin

from dkist_processing_visp.visp_base import VispScienceTask


class WriteQualityReport(VispScienceTask, MetadataStoreMixin):
    def run(self) -> None:
        logging.warning("Writing DUMMY quality report")
        report = [{"name": "dummy", "description": "dummy", "statement": "dummy"}]
        self.metadata_store_add_quality_report(dataset_id=self.dataset_id, quality_report=report)
