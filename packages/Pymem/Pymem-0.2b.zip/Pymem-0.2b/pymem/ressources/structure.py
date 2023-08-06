import ctypes


class LUID(ctypes.Structure):

    _fields_ = [
        ("LowPart", ctypes.c_ulong),
        ("HighPart", ctypes.c_long)
    ]

class LUID_AND_ATTRIBUTES(ctypes.Structure):

    _fields_ = [
        ("Luid", LUID),
        ("Attributes", ctypes.c_ulong),
    ]

class TOKEN_PRIVILEGES(ctypes.Structure):

    _fields_ = [
        ("PrivilegeCount", ctypes.c_ulong),
        ("Privileges", 1 * LUID_AND_ATTRIBUTES)
    ]


class ModuleEntry32(ctypes.Structure):
    """Describes an entry from a list of the modules belonging to the specified process.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684225%28v=vs.85%29.aspx
    """
    _fields_ = [
        ( 'dwSize' , ctypes.c_ulong ) ,
        ( 'th32ModuleID' , ctypes.c_ulong ),
        ( 'th32ProcessID' , ctypes.c_ulong ),
        ( 'GlblcntUsage' , ctypes.c_ulong ),
        ( 'ProccntUsage' , ctypes.c_ulong ) ,
        ( 'modBaseAddr' , ctypes.POINTER(ctypes.c_byte)),
        ( 'modBaseSize' , ctypes.c_ulong ) ,
        ( 'hModule' , ctypes.c_ulong ) ,
        ( 'szModule' , ctypes.c_char * 256 ),
        ( 'szExePath' , ctypes.c_char * 260 )
    ]

    @property
    def base_address(self):
        return ctypes.addressof(self.modBaseAddr.contents)

    @property
    def name(self):
        return self.szModule.decode('utf-8')


class ProcessEntry32(ctypes.Structure):
    """Describes an entry from a list of the processes residing in the system address space when a snapshot was taken.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms684839(v=vs.85).aspx
    """
    _fields_ = [
        ( 'dwSize' , ctypes.c_ulong ) ,
        ( 'cntUsage' , ctypes.c_ulong) ,
        ( 'th32ProcessID' , ctypes.c_ulong) ,
        ( 'th32DefaultHeapID' , ctypes.POINTER(ctypes.c_ulong) ) ,
        ( 'th32ModuleID' , ctypes.c_ulong) ,
        ( 'cntThreads' , ctypes.c_ulong) ,
        ( 'th32ParentProcessID' , ctypes.c_ulong) ,
        ( 'pcPriClassBase' , ctypes.c_long) ,
        ( 'dwFlags' , ctypes.c_ulong) ,
        ( 'szExeFile' , ctypes.c_char * 260 )
    ]

    @property
    def szExeFile(self):
        return self.szExeFile.decode('utf-8')


class ThreadEntry32(ctypes.Structure):
    """Describes an entry from a list of the threads executing in the system when a snapshot was taken.

    https://msdn.microsoft.com/en-us/library/windows/desktop/ms686735(v=vs.85).aspx
    """

    _fields_ = [
        ('dwSize', ctypes.c_ulong),
        ("cntUsage", ctypes.c_ulong),
        ("th32ThreadID", ctypes.c_ulong),
        ("th32OwnerProcessID", ctypes.c_ulong),
        ("tpBasePri", ctypes.c_ulong),
        ("tpDeltaPri", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong)
    ]

    @property
    def szExeFile(self):
        return self.szExeFile.decode('utf-8')


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
    """Undocumented ctypes.Structure used for ThreadContext."""
    _fields_ = [
        ('ControlWord', ctypes.c_uint),
        ('StatusWord', ctypes.c_uint),
        ('TagWord', ctypes.c_uint),
        ('ErrorOffset', ctypes.c_uint),
        ('ErrorSelector', ctypes.c_uint),
        ('DataOffset', ctypes.c_uint),
        ('DataSelector', ctypes.c_uint),
        ('RegisterArea', ctypes.c_byte * SIZE_OF_80387_REGISTERS),
        ('Cr0NpxState', ctypes.c_uint)
    ]

MAXIMUM_SUPPORTED_EXTENSION = 512
class ThreadContext(ctypes.Structure):
    """Represents a thread context"""

    _fields_ = [
        ('ContextFlags', ctypes.c_uint),
        ('Dr0', ctypes.c_uint),
        ('Dr1', ctypes.c_uint),
        ('Dr2', ctypes.c_uint),
        ('Dr3', ctypes.c_uint),
        ('Dr6', ctypes.c_uint),
        ('Dr7', ctypes.c_uint),
        ('FloatSave', FLOATING_SAVE_AREA),
        ('SegGs', ctypes.c_uint),
        ('SegFs', ctypes.c_uint),
        ('SegEs', ctypes.c_uint),
        ('SegDs', ctypes.c_uint),
        ('Edi', ctypes.c_uint),
        ('Esi', ctypes.c_uint),
        ('Ebx', ctypes.c_uint),
        ('Edx', ctypes.c_uint),
        ('Ecx', ctypes.c_uint),
        ('Eax', ctypes.c_uint),
        ('Ebp', ctypes.c_uint),
        ('Eip', ctypes.c_uint),
        ('SegCs', ctypes.c_uint),
        ('EFlags', ctypes.c_uint),
        ('Esp', ctypes.c_uint),
        ('SegSs', ctypes.c_uint),
        ('ExtendedRegisters', ctypes.c_byte * MAXIMUM_SUPPORTED_EXTENSION)
    ]