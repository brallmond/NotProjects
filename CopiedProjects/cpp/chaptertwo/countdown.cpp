#include <iostream>

int main()
{
	std::cout << "Countdown start? " << std::endl;

	int countstart;
	std::cin >> countstart;

	std::cout << "Countdown end? " << std::endl;

	int countend;
	std::cin >> countend;

	std::cout << std::endl;

	for(int i = countstart; i != countend-1; --i)
	{std::cout << i << std::endl;}

	return 0;
}
