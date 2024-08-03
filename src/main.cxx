#include "intelligence.h"

int main(){
    
    DWORD process_count = 0x0;
    
    GetProcessCountViaSnapShot(&process_count);
    
    PRINT("[i] Processes: %ld\n", process_count);
    
    return 0;
}
