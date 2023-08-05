
from owdo.connection import ow

class OWStack:
  def __init__(self, ow, name):
    stack_list = ow.describe_stacks()['Stacks']
    stacks = {}

    for stack in stack_list:
      stacks[stack['Name']] = stack

    self._stack_list = stack_list
    self._stacks = stacks

    self._stack = stacks[name]

  def __getitem__(self, key):
    return self._stack[key]

  def __iter__(self):
    for key in self._stack:
      yield self._stack[key]

class OWLayer:
  def __init__(self, ow, stack, name):
    layer_list =  ow.describe_layers(stack['StackId'])['Layers']
    layers = {}
    for layer in layer_list:
      layers[layer['Name']] = layer

    self._layer_list = layer_list
    self._layers = layers
    self._layer = layers[name]

  def __getitem__(self, key):
    return self._layer[key]

  def __iter__(self):
    for key in self._layer:
      yield self._layer[key]

class OWInstance:
  def __init__(self, ow, stack, layer, name):
    instance_list =  ow.describe_instances(layer_id=layer['LayerId'])['Instances']
    instances = {}
    for instance in instance_list:
      instances[instance['Hostname']] = instance

    self._instance_list = instance_list
    self._instances = instances
    self._instance = instances[name]

  def __getitem__(self, key):
    return self._instance[key]

  def __iter__(self):
    for key in self._instance:
      yield self._instance[key]

