#include <iostream>
#include <unistd.h> // for usleep()

void spin(int time = 2) { //total spin time is approx (time)*(0.6 sec)
for (int i =0; i<time; i++){
		std::cout << '\\' << std::flush; //flush makes the coutput print immediately
		usleep(150000);
		std::cout << '\b' << '|' << std::flush;
		usleep(150000);
		std::cout << '\b' << '/' << std::flush;
		usleep(150000);
		std::cout << '\b' << '|' << std::flush;
		usleep(150000);
		std::cout << '\b' << std::flush;
	}
}
