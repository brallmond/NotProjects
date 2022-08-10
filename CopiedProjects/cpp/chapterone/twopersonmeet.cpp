//two people meet and then greet one another
#include <iostream>
#include <string>

int main() 
{
	std::cout << "C: What is your name? ";

	std::string name;
	std::cin >> name;
	std::cout << "Hello, " << name;
	std::cin >> name; //flushes standard input
	std::cout << std::endl;
	std::cout << "And what is yours? " << std::endl;
	std::cin >> name;
	std::cout << "Hello, " << name << "; nice to meet you too!" << std::endl;
	
	return 0;
}
