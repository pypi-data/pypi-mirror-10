import ctypes
from ctypes import c_byte, c_char, c_long, c_uint, wintypes
from ctypes import POINTER, Structure


class ModuleEntry32(Structure):
    """Describes an entry from a list of the modules belonging to the specified process.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684225%28v=vs.85%29.aspx
    """
    _fields_ = [
        ( 'dwSize' , wintypes.DWORD ) ,
        ( 'th32ModuleID' , wintypes.DWORD ),
        ( 'th32ProcessID' , wintypes.DWORD ),
        ( 'GlblcntUsage' , wintypes.DWORD ),
        ( 'ProccntUsage' , wintypes.DWORD ) ,
        ( 'modBaseAddr' , POINTER(wintypes.BYTE) ) ,
        ( 'modBaseSize' , wintypes.DWORD ) ,
        ( 'hModule' , wintypes.HMODULE ) ,
        ( 'szModule' , c_char * 256 ),
        ( 'szExePath' , c_char * 260 )
    ]

class ProcessEntry32(Structure):
    """Describes an entry from a list of the processes residing in the system address space when a snapshot was taken.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684839(v=vs.85).aspx
    """
    _fields_ = [
        ( 'dwSize' , wintypes.DWORD ) ,
        ( 'cntUsage' , wintypes.DWORD) ,
        ( 'th32ProcessID' , wintypes.DWORD) ,
        ( 'th32DefaultHeapID' , POINTER(ctypes.c_ulong)) ,
        ( 'th32ModuleID' , wintypes.DWORD) ,
        ( 'cntThreads' , wintypes.DWORD) ,
        ( 'th32ParentProcessID' , wintypes.DWORD) ,
        ( 'pcPriClassBase' , wintypes.LONG) ,
        ( 'dwFlags' , wintypes.DWORD) ,
        ( 'szExeFile' , c_char * 260 )
    ]

    @property
    def szExeFile(self):
        return self.szExeFile.decode('utf-8')


class ThreadEntry32(ctypes.Structure):
    """Describes an entry from a list of the threads executing in the system when a snapshot was taken.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735(v=vs.85).aspx
    """

    _fields_ = [
        ('dwSize', wintypes.DWORD),
        ("cntUsage", wintypes.DWORD),
        ("th32ThreadID", wintypes.DWORD),
        ("th32OwnerProcessID", wintypes.DWORD),
        ("tpBasePri", wintypes.DWORD),
        ("tpDeltaPri", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD)
    ]


class PROCESS(object):
    """Process manipulation flags"""

    #: Required to create a process.
    PROCESS_CREATE_PROCESS = 0x0080
    #: Required to create a thread.
    PROCESS_CREATE_THREAD = 0x0002
    #: PROCESS_DUP_HANDLE
    PROCESS_DUP_HANDLE = 0x0040
    #: Required to retrieve certain information about a process, such as its token, exit code, and priority class (see OpenProcessToken).
    PROCESS_QUERY_INFORMATION = 0x0400
    #: Required to retrieve certain information about a process (see GetExitCodeProcess, GetPriorityClass, IsProcessInJob, QueryFullProcessImageName).
    PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
    #: Required to set certain information about a process, such as its priority class (see SetPriorityClass).
    PROCESS_SET_INFORMATION = 0x0200
    #: Required to set memory limits using SetProcessWorkingSetSize.
    PROCESS_SET_QUOTA = 0x0100
    #: Required to suspend or resume a process.
    PROCESS_SUSPEND_RESUME = 0x0800
    #: Required to terminate a process using TerminateProcess.
    PROCESS_TERMINATE = 0x0001
    #: Required to perform an operation on the address space of a process (see VirtualProtectEx and WriteProcessMemory).
    PROCESS_VM_OPERATION = 0x0008
    #: Required to read memory in a process using ReadProcessMemory.
    PROCESS_VM_READ = 0x0010
    #: Required to write to memory in a process using WriteProcessMemory.
    PROCESS_VM_WRITE = 0x0020
    #: Required to wait for the process to terminate using the wait functions.
    SYNCHRONIZE = 0x00100000
    #: All possible access rights for a process object.
    PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
    #: Required to delete the object.
    DELETE = 0x00010000
    #: Required to read information in the security descriptor for the object, not including the information in the SACL. To read or write the SACL, you must request the ACCESS_SYSTEM_SECURITY access right. For more information, see SACL Access Right.
    READ_CONTROL = 0x00020000
    #: Required to modify the DACL in the security descriptor for the object.
    WRITE_DAC = 0x00040000
    #: Required to change the owner in the security descriptor for the object.
    WRITE_OWNER = 0x00080000

class MemoryAllocation(object):
    """The type of memory allocation
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa366890%28v=vs.85%29.aspx"""

    #: Allocates memory charges (from the overall size of memory and the paging files on disk) for the specified reserved memory pages. The function also guarantees that when the caller later initially accesses the memory, the contents will be zero. Actual physical pages are not allocated unless/until the virtual addresses are actually accessed.
    MEM_COMMIT = 0x00001000
    #: Reserves a range of the process's virtual address space without allocating any actual physical storage in memory or in the paging file on disk.
    MEM_RESERVE = 0x00002000
    #: Indicates that data in the memory range specified by lpAddress and dwSize is no longer of interest. The pages should not be read from or written to the paging file. However, the memory block will be used again later, so it should not be decommitted. This value cannot be used with any other value.
    MEM_RESET = 0x00080000
    #: MEM_RESET_UNDO should only be called on an address range to which MEM_RESET was successfully applied earlier. It indicates that the data in the specified memory range specified by lpAddress and dwSize is of interest to the caller and attempts to reverse the effects of MEM_RESET. If the function succeeds, that means all data in the specified address range is intact. If the function fails, at least some of the data in the address range has been replaced with zeroes.
    MEM_RESET_UNDO = 0x1000000
    #: Allocates memory using large page support.
    MEM_LARGE_PAGES = 0x20000000
    #: Reserves an address range that can be used to map Address Windowing Extensions (AWE) pages.
    MEM_PHYSICAL = 0x00400000
    #: Allocates memory at the highest possible address. This can be slower than regular allocations, especially when there are many allocations.
    MEM_TOP_DOWN = 0x00100000
    MEM_DECOMMIT = 0x4000
    MEM_RELEASE = 0x8000

class MemoryProtection(object):
    """The following are the memory-protection options;
    you must specify one of the following values when allocating or protecting a page in memory
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa366786(v=vs.85).aspx"""

    #: Enables execute access to the committed region of pages. An attempt to write to the committed region results in an access violation.
    PAGE_EXECUTE = 0x10
    #: Enables execute or read-only access to the committed region of pages. An attempt to write to the committed region results in an access violation.
    PAGE_EXECUTE_READ = 0x20
    #: Enables execute, read-only, or read/write access to the committed region of pages.
    PAGE_EXECUTE_READWRITE = 0x40
    #: Enables execute, read-only, or copy-on-write access to a mapped view of a file mapping object. An attempt to write to a committed copy-on-write page results in a private copy of the page being made for the process. The private page is marked as PAGE_EXECUTE_READWRITE, and the change is written to the new page.
    PAGE_EXECUTE_WRITECOPY = 0x80
    #: Disables all access to the committed region of pages. An attempt to read from, write to, or execute the committed region results in an access violation.
    PAGE_NOACCESS = 0x01
    #: Enables read-only access to the committed region of pages. An attempt to write to the committed region results in an access violation. If Data Execution Prevention is enabled, an attempt to execute code in the committed region results in an access violation.
    PAGE_READONLY = 0x02
    #: Enables read-only or read/write access to the committed region of pages. If Data Execution Prevention is enabled, attempting to execute code in the committed region results in an access violation.
    PAGE_READWRITE = 0x04
    #: Enables read-only or copy-on-write access to a mapped view of a file mapping object. An attempt to write to a committed copy-on-write page results in a private copy of the page being made for the process. The private page is marked as PAGE_READWRITE, and the change is written to the new page. If Data Execution Prevention is enabled, attempting to execute code in the committed region results in an access violation.
    PAGE_WRITECOPY = 0x08
    #: Pages in the region become guard pages. Any attempt to access a guard page causes the system to raise a STATUS_GUARD_PAGE_VIOLATION exception and turn off the guard page status. Guard pages thus act as a one-time access alarm. For more information, see Creating Guard Pages.
    PAGE_GUARD = 0x100
    #: Sets all pages to be non-cachable. Applications should not use this attribute except when explicitly required for a device. Using the interlocked functions with memory that is mapped with SEC_NOCACHE can result in an EXCEPTION_ILLEGAL_INSTRUCTION exception.
    PAGE_NOCACHE = 0x200
    #: Sets all pages to be write-combined.
    #: Applications should not use this attribute except when explicitly required for a device. Using the interlocked functions with memory that is mapped as write-combined can result in an EXCEPTION_ILLEGAL_INSTRUCTION exception.
    PAGE_WRITECOMBINE = 0x400


SIZE_OF_80387_REGISTERS = 80
class FLOATING_SAVE_AREA(ctypes.Structure):
    """Undocumented structure used for ThreadContext."""
    _fields_ = [
        ('ControlWord', c_uint),
        ('StatusWord', c_uint),
        ('TagWord', c_uint),
        ('ErrorOffset', c_uint),
        ('ErrorSelector', c_uint),
        ('DataOffset', c_uint),
        ('DataSelector', c_uint),
        ('RegisterArea', c_byte * SIZE_OF_80387_REGISTERS),
        ('Cr0NpxState', c_uint)
    ]

MAXIMUM_SUPPORTED_EXTENSION = 512
class ThreadContext(ctypes.Structure):
    """Represents a thread context"""

    _fields_ = [
        ('ContextFlags', c_uint),
        ('Dr0', c_uint),
        ('Dr1', c_uint),
        ('Dr2', c_uint),
        ('Dr3', c_uint),
        ('Dr6', c_uint),
        ('Dr7', c_uint),
        ('FloatSave', FLOATING_SAVE_AREA),
        ('SegGs', c_uint),
        ('SegFs', c_uint),
        ('SegEs', c_uint),
        ('SegDs', c_uint),
        ('Edi', c_uint),
        ('Esi', c_uint),
        ('Ebx', c_uint),
        ('Edx', c_uint),
        ('Ecx', c_uint),
        ('Eax', c_uint),
        ('Ebp', c_uint),
        ('Eip', c_uint),
        ('SegCs', c_uint),
        ('EFlags', c_uint),
        ('Esp', c_uint),
        ('SegSs', c_uint),
        ('ExtendedRegisters', c_byte * MAXIMUM_SUPPORTED_EXTENSION)
    ]