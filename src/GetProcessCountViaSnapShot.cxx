BOOL GetProcessCountViaSnapShot(OUT DWORD* dwProcessCount) {

	PROCESSENTRY32  ProcEntry						= { .dwSize = sizeof(PROCESSENTRY32) };
	HANDLE			hSnapShot						= INVALID_HANDLE_VALUE;
    DWORD           dwProcCount                     = 0x0;

	if (!dwUniqueProcessCount){
		return FALSE;
    }

	if ((hSnapShot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL)) == INVALID_HANDLE_VALUE) {
		PRINT("[!] CreateToolhelp32Snapshot Failed With Error: %d \n", GetLastError());
		return FALSE;
	}

	if (!Process32First(hSnapShot, &ProcEntry)) {
		PRINT("[!] Process32First Failed With Error: %d \n", GetLastError());
		goto _END_OF_FUNC;
	}

	do {

		dwProcCount++;

	} while (Process32Next(hSnapShot, &ProcEntry));

    *dwProcessCount = dwProcCount;

_END_OF_FUNC:
	if (hSnapShot != INVALID_HANDLE_VALUE){
		CloseHandle(hSnapShot);
    }
    
	return (*dwProcessCount) ? TRUE : FALSE;
}
