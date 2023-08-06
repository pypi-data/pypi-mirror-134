"""Even quicker way to get webservices, docker containers and GUIs from opyrator

``opyrator`` allows us to write code like this:

>>> from pydantic import BaseModel
>>>
>>> class Input(BaseModel):
...     message: str
...
>>> class Output(BaseModel):
...     message: str
...
>>> def hello_world(input: Input) -> Output:
...     'Returns the `message` of the input data.'
...     return Output(message=input.message)

Putting this in a file named ``my_opurator.py`` and running

.. code-block::
    opyrator launch-ui my_opyrator:hello_world


from the command-line, we get a fully functional web GUI for the `hello_world` function.

But to use `opyrator` you need to make those input and output models by hand.
Or do you?...

"""
