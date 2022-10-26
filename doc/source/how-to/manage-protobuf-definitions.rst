Manage Protobuf Definitions
===========================

Protobuf service definitions provide the API specification for underlying
server implementations, so that each consuming client library has a clear
contract for gRPC data messages. Ideally, the proto files have a single
repository established as the source of truth for the .proto files,
organized by API version increment as the API definition expands and changes.
Since most client libraries are custom implementations enhancing the developer
experience when consuming the service, releasing the Protobuf definitions
publicly gives full flexibility to the developer to operate at the abstraction
layer they choose to do so.


Managing proto definitions for Python clients
---------------------------------------------

Maintain API definition repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build Python stub classes
~~~~~~~~~~~~~~~~~~~~~~~~~

Publish Python API package
~~~~~~~~~~~~~~~~~~~~~~~~~~

Consume API package within Python client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

