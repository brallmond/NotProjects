#include <iostream>

int main()
{
	std::cout << "Give me two numbers and I'll tell you which is larger (meaning farther along on the positive side of a number line)." <<std::endl;

	float numberOne;
	std::cout << "First number: " << std::endl;
	std::cin >> numberOne;

	float numberTwo;
	std::cout << "Second number: " << std::endl;
	std::cin >> numberTwo;

	if(numberOne == numberTwo || numberOne > numberTwo)
	{
		if(numberOne > numberTwo)
		{std::cout << numberOne << " is greater than " << numberTwo << std::endl;}
		else{std::cout << numberOne << " is equal to " << numberTwo << std::endl;}
	}
	else{std::cout << numberTwo << " is greater than " << numberOne << std::endl;}

	return 0;
}
