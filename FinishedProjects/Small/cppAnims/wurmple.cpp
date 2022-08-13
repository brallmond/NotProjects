#include <iostream>
#include <unistd.h> //for usleep

void wurmple(int length = 5, char tmp = '*'){

	for (int i = 0; i < length; i++){
		std::cout << tmp << std::flush;
		usleep(150000);
	}
	for (int i = 0; i<length; i++){
		std::cout << '\b' << std::flush;
		std::cout << ' ' << '\b'  << std::flush;
		usleep(150000);
	}

}
