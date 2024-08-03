#include "intelligence.h"

int main(){
    
    DWORD process_count = 0x0;
    
    GetProcessCountViaSnapShot(&proc_count);
    
    PRINT("[i] Processes: %d\n", process_count);
    
    return 0;
}
