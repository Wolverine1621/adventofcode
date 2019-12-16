#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;

int64_t recursiveWeight(uint64_t input) {
	int64_t weight = input / 3 - 2;
	if (weight < 0) {
		return 0;
	}

	return weight + recursiveWeight(weight);
}

int main() {
	int64_t total = 0;
	int64_t curr_input;

	while (cin >> curr_input) {
		//Part 1: total += (curr_input / 3 - 2);
		total += recursiveWeight(curr_input);
	}

	cout << total << '\n';
	return 0;
}
