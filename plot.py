from matplotlib import pyplot as plt

hardness = [x for x in range(1,7)]
nonce = [11, 586 , 2404, 40128, 621928, 28408962]

plt.figure()
plt.xlabel("Broj nula u hashu")
plt.ylabel("NONCE")

plt.plot(hardness,nonce)

plt.tight_layout()
plt.savefig("output.png")

