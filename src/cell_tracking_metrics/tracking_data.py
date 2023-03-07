class TrackingData:
    def __init__(self, tracking_graph, segmentation=None):
        """A container for tracking output. Must contain a TrackGraph
        with valid tracks. Can contain a numpy-like segmentation.

        Args:
        ----
            tracking_graph (TrackingGraph): A TrackGraph that contains
                nodes indicating cell detections and edges indicating links between
                detections over time.
            segmentation (numpy-like array, optional): A numpy-like array of segmentations.
                The location of each node in tracking_graph is assumed to be inside the
                area of the corresponding segmentation. Defaults to None.
        """
        self.tracking_graph = tracking_graph
        self.segmentation = segmentation