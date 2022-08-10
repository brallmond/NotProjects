// ask for a person's name, and greet the person fancily
#include <iostream>
#include <string>

int main()
{
	std:: cout << "Please enter your first name: ";
	std::string name;
	std::cin >> name;

	//build the message that we want
	const std::string greeting = "Hello, " + name + ", I'm Estrogen!";

	//build the second and fourth strings
	const std::string spaces(greeting.size(), ' ');
	const std::string second = "* " + spaces + " *";

	//build the first and fifth lines of the output
	const std::string first(second.size(), '*');

	//write it
	std::cout << std::endl;
	std::cout << first << std::endl;
	std::cout << second << std::endl;
	std::cout << "* " << greeting << " *" << std::endl;
	std::cout << second << std::endl;
	std::cout << first << std::endl;

	return 0;
}
