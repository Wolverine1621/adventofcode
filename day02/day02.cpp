#include <iostream>
#include "../Intcode.h"

using namespace std;

void part1(Intcode& vm) {
	vm.loadProgram();
	vm.injectMem(1, 12);
	vm.injectMem(2, 2);

	vm.run();
	vm.printAddr(0);
}

void part2(Intcode& vm) {
	vm.loadProgram();
	for (int i = 0; i < 100; ++i) {
		for (int j = 0; j < 100; ++j) {
			vm.injectMem(1, i);
			vm.injectMem(2, j);
			vm.run();
			
			if (vm.memAt(0) == 19690720) {
				cout << 100 * i + j << '\n';
				exit(0);
			}
			//cout << vm.memAt(0) << " " << vm.memAt(1) << " " << vm.memAt(2) << "\n";

			vm.reload();
		}
	}
}

int main() {
	Intcode vm;
	//part1(vm);
	part2(vm);

	return 0;
}
