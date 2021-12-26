#include <iostream>
#include <unistd.h> //for usleep

void flapper(int time = 3){
	for (int i = 0; i < time; i++){
		std::cout << '\\' << '_' << '/' << '\b' << '\b' << '\b' << std::flush;
		usleep(200000);
		std::cout << ' ' << ' ' << ' ' <<  '\b' << '\b' << '\b' << std::flush;
		std::cout <<'-' << '_' << '-' << '\b' << '\b' << '\b' << std::flush;
		usleep(200000);
		std::cout << ' ' << ' ' << ' ' << '\b' << '\b' << '\b' << std::flush;
		std::cout << '_' << '_' << '_' << '\b' << '\b' << '\b' << std::flush;
		usleep(200000);
		std::cout << ' ' << ' ' << ' ' <<  '\b' << '\b' << '\b' << std::flush;
		std::cout <<'-' << '_' << '-' << '\b' << '\b' << '\b' << std::flush;
		usleep(200000);

	}
}

int main(){
	flapper();
	return 0;
}
