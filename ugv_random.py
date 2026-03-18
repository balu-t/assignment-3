import random

def generate_grid(size, density):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            if random.random() < density:
                row.append(1)  # obstacle
            else:
                row.append(0)
        grid.append(row)
    return grid


size = 10

print("Low density grid:")
print(generate_grid(size, 0.2))

print("\nMedium density grid:")
print(generate_grid(size, 0.4))

print("\nHigh density grid:")
print(generate_grid(size, 0.6))
