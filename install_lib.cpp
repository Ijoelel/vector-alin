#include <iostream>

int main(){
	system("pip install Pillow");
	system("pip install matplotlib");
	system("pip install pdf2image");
	system("move poppler C:\\");
	system("pwsh -Command \"$path = [Environment]::GetEnvironmentVariable(\'PATH\', \'Machine\'); echo $path ; $poppler_path = \'C:/poppler/Library/bin\'; echo $poppler_path ; [Environment]::SetEnvironmentVariable(\'Path\', \\\"$path;$poppler_path\\\", \'Machine\')\"");
	

	return 0;
}