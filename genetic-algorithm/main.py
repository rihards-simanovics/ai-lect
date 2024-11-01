import random
import string


class StringGeneticAlgorithm:
    def __init__(self, target, population_size=100, mutation_rate=0.01):
        self.__target = target
        self.__population_size = population_size
        self.__mutation_rate = mutation_rate
        self.__population = self.__initialise_population()
        self.__generation = 0

    def __initialise_population(self):
        # Generate a random initial population of strings
        population = []
        for _ in range(self.__population_size):
            random_string = "".join(
                random.choice(string.ascii_lowercase) for _ in range(len(self.__target))
            )
            population.append(random_string)
        return population

    def __fitness(self, individual):
        # Calculate fitness based on how many characters match the target string
        return sum(1 for i, j in zip(individual, self.__target) if i == j)

    def __selection(self):
        # Select individuals based on fitness using roulette wheel selection
        fitnesses = [self.__fitness(ind) for ind in self.__population]
        total_fitness = sum(fitnesses)
        probabilities = [f / total_fitness for f in fitnesses]
        return random.choices(
            self.__population, weights=probabilities, k=self.__population_size
        )

    def __crossover(self, parent1, parent2):
        # Perform single-point crossover
        point = random.randint(1, len(self.__target) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    def __mutation(self, individual):
        # Mutate the individual by randomly changing characters based on the mutation rate
        return "".join(
            (
                char
                if random.random() > self.__mutation_rate
                else random.choice(string.ascii_lowercase)
            )
            for char in individual
        )

    def __replacement(self, offspring):
        # Replace the current population with the new offspring
        self.__population = offspring

    def __termination_criteria(self):
        # Terminate if any individual matches the target string
        return any(ind == self.__target for ind in self.__population)

    def run(self):
        # Main loop of the genetic algorithm
        while not self.__termination_criteria():
            self.__generation += 1
            selected = self.__selection()

            offspring = []
            for i in range(0, len(selected), 2):
                parent1 = selected[i]
                parent2 = selected[i + 1] if i + 1 < len(selected) else selected[i]
                child1, child2 = self.__crossover(parent1, parent2)
                offspring.append(self.__mutation(child1))
                offspring.append(self.__mutation(child2))

            self.__replacement(offspring)

            # Output the best individual and its fitness at each generation
            best_individual = max(self.__population, key=self.__fitness)
            print(
                f"Generation: {self.__generation}, Best: {best_individual}, Fitness: {self.__fitness(best_individual)}"
            )

        print(
            f"Target string '{self.__target}' achieved in {self.__generation} generations."
        )


# Example usage
if __name__ == "__main__":
    target_string = "zistisfantastish"
    ga = StringGeneticAlgorithm(target=target_string)
    ga.run()
