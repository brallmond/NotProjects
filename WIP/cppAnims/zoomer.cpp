#include <iostream>
#include <unistd.h> // for usleep

void zoomer(int end = 8, int rep = 3, char tmp = '*'){
	for (int j = 0; j < rep; j++){ //repeat the whole thing
		for (int i = 0; i < end; i++){ //go forward
			std::cout << tmp << std::flush;
			usleep(150000);
			std::cout << '\b' << ' ' << std::flush;
		}
		
		for (int i = 0; i < end; i++){ //go back
			std::cout << '\b' << tmp << std::flush;
			usleep(150000);
			std::cout << '\b' << ' ' << std::flush;
			std::cout << '\b' << std::flush;
		}
	}
}
