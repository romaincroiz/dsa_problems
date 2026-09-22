import pytest

from dsa.solutions.heap.rsc_allocation import RscManager


class TestRscManager:

    __rsc_manager = RscManager()

    def test_deallocate_throws_exception_when_not_found(self):
        with pytest.raises(IndexError):
            self.__rsc_manager.deallocate("host_10")

    def test_deallocate_when_found(self):
        self.__rsc_manager.allocate("host")
        self.__rsc_manager.deallocate("host_1")
        assert not self.__rsc_manager.is_allocated("host_1")

    def test_reallocate_deallocated_rsc(self):
        self.__rsc_manager.allocate("host") # 1
        self.__rsc_manager.allocate("host") # 1, 2
        self.__rsc_manager.allocate("host") # 1, 2, 3

        self.__rsc_manager.deallocate("host_2") # 1, 3
        self.__rsc_manager.allocate("host")  # 1, 2, 3

        assert self.__rsc_manager.is_allocated("host_1")
        assert self.__rsc_manager.is_allocated("host_2")
        assert self.__rsc_manager.is_allocated("host_3")

    def test_example1(self):
        self.__rsc_manager.allocate("host")  # {host_1}
        self.__rsc_manager.allocate("host")  # {host_1, host_2}
        self.__rsc_manager.allocate("host")  # {host_1, host_2, host_3}
        self.__rsc_manager.allocate("api")  # {host_1, host_2, host_3}, {api_1}
        self.__rsc_manager.deallocate("host_3")  # {host_1, host_2}, {api_1}
        self.__rsc_manager.allocate("host")  # {host_1, host_2, host_3}, {api_1}
        self.__rsc_manager.allocate("api")  # {host_1, host_2, host_3}, {api_1,api_2}
        self.__rsc_manager.deallocate("api_1")  # {host_1, host_2, host_3}, {api_2}
        self.__rsc_manager.deallocate("api_2")  # {host_1, host_2, host_3}

        assert self.__rsc_manager.is_allocated("host_1")
        assert self.__rsc_manager.is_allocated("host_2")
        assert self.__rsc_manager.is_allocated("host_3")
        assert not self.__rsc_manager.is_allocated("api_1")
        assert not self.__rsc_manager.is_allocated("api_2")

    def test_example2(self):
        self.__rsc_manager.allocate("host")  # {host_1}
        self.__rsc_manager.allocate("host")  # {host_1, host_2}
        self.__rsc_manager.allocate("host")  # {host_1, host_2, host_3}
        self.__rsc_manager.deallocate("host_2")  # {host_1, host_3}

        self.__rsc_manager.allocate("host")  # {host_1, host_2, host_3}
        self.__rsc_manager.deallocate("host_1")  # {host_2, host_3}

        self.__rsc_manager.allocate("host")  # {host_1, host_2, host_3}
        self.__rsc_manager.allocate("host")  # {host_1, host_2, host_3, host4}
        self.__rsc_manager.deallocate("host_1")  # {host_2, host_3, host4}
        self.__rsc_manager.deallocate("host_3")  # {host_2, host4}

        assert not self.__rsc_manager.is_allocated("host_1")
        assert not self.__rsc_manager.is_allocated("host_3")
        assert self.__rsc_manager.is_allocated("host_2")
        assert self.__rsc_manager.is_allocated("host_4")

    def test_example3(self):
        self.__rsc_manager.allocate("host")  # {host_1}
        self.__rsc_manager.allocate("host")  # {host_1, host_2}
        self.__rsc_manager.allocate("host")  # {host_1, host_2, host_3}
        self.__rsc_manager.deallocate("host_2")  # {host1, host_3}
        with pytest.raises(IndexError):
            self.__rsc_manager.deallocate("host_2")