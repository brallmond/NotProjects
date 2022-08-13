#include <iostream>
#include <unistd.h> // for usleep
#include <string> // for length

void wordgen(std::string word = "hello"){
	word.push_back(' ');
	for (int i = 0; i < word.length(); i++){
		std::cout << word[i] << std::flush;
		usleep(300000);
	}
	std::cout << std::endl;
}
