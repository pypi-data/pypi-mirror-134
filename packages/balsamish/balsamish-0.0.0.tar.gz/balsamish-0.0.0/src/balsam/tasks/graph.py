from abc import ABC, abstractmethod


def to_snake_case(s):
    # TODO: implement and move to utils
    return s


class AbstractChannel(ABC):
    """Interface for channels."""

    @abstractmethod
    def put(self, context, name, value):
        pass

    @abstractmethod
    def get(self, context, name):
        pass


class InMemoryChannel(AbstractChannel):
    def __init__(self):
        self._stored = {}

    def put(self, task_name, value_name, value):
        if task_name in self._stored:
            pass


class TaskGraph:
    """
    Builds an abstract directed task graph.  The graph may then be instantiated
    as a concrete program in open-ended ways, e.g., as a single
    :class:`~AbstractTask` instance, or as an Airflow DAG.  Instantiation is
    essentially a process of interpretation of the graph in different contexts.

    The nodes of the graph are abstract tasks, preferably pure computations,
    while the arcs go from an output of one task to an input of another.  The
    effects that might be needed to do the actual transfer of data are in the
    interpretation of the arcs.  For example, storing and retrieving
    intermediate results on S3, in the case of interpretation in an Airflow DAG.
    """

    def __init__(self):
        self.nodes = {}
        self.arcs = {}

    def insert(self, task, task_name=None, inputs=None):
        """Inserts a task as a node and connects it to the outputs of an already
        inserted task.

        :param task: The task to insert.  Should be an instance of
            :class:`~AbstractTask`.
        :param task_name: The name of the node that represents the task.  Should
            not exist yet. Defaults to the snake_cased name of the class.
        :param inputs: A dictionary of inputs. Defaults to no inputs.

        >> graph = TaskGraph()
        >> outputs = graph.insert(FirstTask())
        >> graph.insert(SecondTask(), {"train_data": outputs["raw_data"]})

        :raises ValueError: If there is already a node with name `task_name` in
            the graph, or when the specified inputs do not match the expected
            inputs of the task.
        """
        self._check_inputs(task, inputs)
        node_name = task_name or to_snake_case(task.__class__.__name__)
        self.nodes[node_name] = task

        return self._create_outputs(task, node_name)

    def _check_inputs(self, task, inputs):
        # TODO: check whether the input specification (in terms of a
        # balsam.schema) matches the expected inputs for the task, and check
        # whether the producer already exists as a node name in the graph.
        pass

    def _create_outputs(self, task, node_name):
        return {
            name: {
                'schema': schema,
                'producer': node_name
            }
            for (name, schema) in task.output_schema.items()
        }


## === EXAMPLE CLIENT ====

# def create_graph():
#     graph = TaskGraph()
#     task1_outputs = graph.insert(Task1())
#     task2_outputs = graph.insert(Task2(),
#                                  {'bid_landscape': task2_outputs['bid_landscape']})
