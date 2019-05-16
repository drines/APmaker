import json
from autoprotocol.protocol import Protocol

# instantiate a protocol object
p = Protocol()

# generate a ref
# specify where it comes from and how it should be handled when the Protocol is done
plate = p.ref("A000001", id="A000001", cont_type="96-pcr", discard=True)

# generate seal and spin instructions that act on the ref
# some parameters are explicitly specified and others are left to vendor defaults
p.seal(
    ref=plate,
    type="foil",
    mode="thermal",
    temperature="165:celsius",
    duration="1.5:seconds"
)
p.spin(
    ref=plate,
    acceleration="1000:g",
    duration="1:minute"
)

print(p)

# serialize the protocol as Autoprotocol JSON
print(json.dumps(p.as_dict(), indent=2))