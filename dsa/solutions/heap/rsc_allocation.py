from data_structure.ds_min_heap import DsMinHeap

RSC_SEP = "_"


class RscManager:

    # set of allocated resource names
    __allocated: set[str]
    # map deallocated resource type > ids
    __deallocated: dict[str, DsMinHeap]
    # next 'unused' id available for each resource type
    __next_id: dict[str, int]

    def __init__(self):
        self.__allocated = set()
        self.__deallocated = {}
        self.__next_id = {}

    def allocate(self, rsc_type):
        if rsc_type not in self.__next_id:
            self.__next_id[rsc_type] = 1
        lowest_available_id = self.__next_id[rsc_type]
        if rsc_type in self.__deallocated and not self.__deallocated[rsc_type].is_empty():
            lowest_available_id = self.__deallocated[rsc_type].poll()
        else:
            self.__next_id[rsc_type]+=1
        resource_name = f"{rsc_type}{RSC_SEP}{lowest_available_id}"
        self.__allocated.add(resource_name)

    def deallocate(self, rsc_name):
        if self.is_allocated(rsc_name):
            self.__allocated.remove(rsc_name)
            rsc_type = rsc_name.split(RSC_SEP)[0]
            rsc_id = rsc_name.split(RSC_SEP)[1]
            if rsc_type not in self.__deallocated:
                self.__deallocated[rsc_type] = DsMinHeap()
            self.__deallocated[rsc_type].add(rsc_id)
        else:
            raise IndexError(f"Resource {rsc_name} not found")

    def is_allocated(self, rsc_name) -> bool:
        return rsc_name in self.__allocated