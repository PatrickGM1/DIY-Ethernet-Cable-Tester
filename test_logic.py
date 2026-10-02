from tester import analyze, B

good = [{b} for b in B]

swapped = list(good)
swapped[0], swapped[1] = {B[1]}, {B[0]}

opened = list(good)
opened[2] = set()

shorted = list(good)
shorted[4] = {B[4], B[5]}

for name, data in [("good", good), ("swapped", swapped),
                   ("open", opened), ("short", shorted)]:
    print(name, analyze(data))