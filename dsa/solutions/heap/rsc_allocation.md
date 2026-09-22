# Resources allocation

## Problem

We want to manage resources in a system with the following:
- allocate(rsc_type): adds a new resource of type `rsc_type` at the lowest available slot
- deallocate(rsc_name): remove the resource from the allocated resources

## Examples

### Example 1

```python
allocate("host") # {host_1}
allocate("host") # {host_1, host_2}
allocate("host") # {host_1, host_2, host_3}
allocate("api")  # {host_1, host_2, host_3}, {api_1}
deallocate("host_3")  # {host_1, host_2}, {api_1}
allocate("host")  # {host_1, host_2, host_3}, {api_1}
allocate("api")  # {host_1, host_2, host_3}, {api_1,api_2}
deallocate("api_1")  # {host_1, host_2, host_3}, {api_2}
deallocate("api_2")  # {host_1, host_2, host_3}
```

### Example 2

```python
allocate("host") # {host_1}
allocate("host") # {host_1, host_2}
allocate("host") # {host_1, host_2, host_3}
deallocate("host_2") # {host_1, host_3}
allocate("host")  # {host_1, host_2, host_3}
deallocate("host_1") # {host_2, host_3}
allocate("host")  # {host_1, host_2, host_3}
allocate("host")  # {host_1, host_2, host_3, host4}
```

### Example 3

```python
allocate("host") # {host_1}
allocate("host") # {host_1, host_2}
allocate("host") # {host_1, host_2, host_3}
deallocate("host_2") # {host_1, host_3}
deallocate("host_2") # Error: Resource host_2 is not allocated
```


## Constraints

- no duplicated resources (same name) in the system
- a resource name is formed by type_id
- 1 > id > Integer.MAX


## Intuition

- resources must be categorized by type → set or dict
- allocate needs to find the lowest available id
- deallocate can set intermediate ids available

### Naive solution: Time O(n), Space O(n)

- One counter per type → dict(type,next_id)
- deallocated: dict(type, list(id)
- allocated: dict(type, list(id)
- Upon allocation of a type, check deallocated list first
- if any deallocated, scan for the lowest > O(n)
- if no, get next_id
- Upon deallocation, scan until find right one and update deallocated

### Optimized solution: Min heap + Set → Time O(logN), O(n)

- One counter per type → dict(type,next_id)
- Min heap deallocated to keep track of lowest deallocated rsc: dict(type, min_heap(id)
- Set of allocated resources for fast deallocation: O(1)
- Upon allocation, check first the deallocated min_heap
- If not empty, pop first id and use it
- otherwise, use next_id
- Upon deallocation, push the id in the min_heap



