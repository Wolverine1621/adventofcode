#ifndef INTCODE_VM
#define INTCODE_VM

#include <iostream>
#include <vector>
#include <string>
#include <cstring>

class Intcode {
public:
	// OPCODES
	static constexpr int OPC_ADD = 1;
	static constexpr int OPC_MULT = 2;
	static constexpr int OPC_HALT = 99;

	void loadProgram() {
		std::string current;
		
		while (std::getline(std::cin, current, ',')) {
			instrMem.push_back(std::stoi(current));
		}

		archive = instrMem;
	}

	void reload() {
		instrMem = archive;
		haltFlag = false;
	}

	void injectMem(size_t pos, int val) {
		instrMem.at(pos) = val;
	}

	int memAt(size_t pos) {
		return instrMem.at(pos);
	}


	void run() {
		for (size_t i = 0; i < instrMem.size() - 4; i += 4) {
			int opc = instrMem.at(i);
			int arg1 = instrMem.at(i + 1);
			int arg2 = instrMem.at(i + 2);
			int arg3 = instrMem.at(i + 3);	

			switch(opc) {
				case OPC_ADD:
					add(arg1, arg2, arg3);
					break;
				case OPC_MULT:
					mult(arg1, arg2, arg3);
					break;
				case OPC_HALT:
					halt();
					break;
				default:
					std::cerr << "ERROR: invalid OPC\n";
					break;
			}

			if (haltFlag) {
				return;
			}
		}
	}

	void printAddr(int address) {
		std::cout << instrMem.at(address) << '\n';
	}

	void printMem() {
		for (int& i : instrMem) {
			std::cout << i << '\n';
		}
	}

private:
	std::vector<int> instrMem;
	std::vector<int> archive;
	bool haltFlag = false;

	void add(int arg1, int arg2, int dest) {
		int result = instrMem.at(arg1) + instrMem.at(arg2);
		instrMem.at(dest) = result;
	}

	void mult(int arg1, int arg2, int dest) {
		int result = instrMem.at(arg1) * instrMem.at(arg2);
		instrMem.at(dest) = result;
	}

	void halt() {
		haltFlag = true;	
	}
};
#endif
