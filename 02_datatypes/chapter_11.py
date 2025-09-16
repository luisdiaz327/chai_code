import arrow
from collections import namedtuple

time = arrow.utcnow()
time.to("Europe/Rome")

print(time)

chaipro = namedtuple("chaipro", ["flavor", "aroma"])
print(chaipro)

