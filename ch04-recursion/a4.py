# 4 - Recursion

## 4.1 - Examples

### 4.1.1 - Factorial
"""
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
"""

### 4.1.2 - Ruler
'''
def draw_line(tick_length, tick_label=''):
  """Draw one line with given tick length (followed by optional label)."""
  line = '-' * tick_length
  if tick_label:
    line += ' ' + tick_label
  print(line)

def draw_interval(center_length):
  """Draw tick interval based upon a central tick length."""
  if center_length > 0:                   # stop when length drops to 0
    draw_interval(center_length - 1)      # recursively draw top ticks
    draw_line(center_length)              # draw center tick
    draw_interval(center_length - 1)      # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
  """Draw English ruler with given number of inches and major tick length."""
  draw_line(major_length, '0')            # draw inch 0 line
  for j in range(1, 1 + num_inches):
    draw_interval(major_length - 1)       # draw interior ticks for inch
    draw_line(major_length, str(j))       # draw inch j line and label


if __name__ == '__main__':
  draw_ruler(2,4)
  print('='*30)
  draw_ruler(1,5)
  print('='*30)
  draw_ruler(3,3)
'''

### 4.1.3 - Binary Search
'''
def binary_search(data, target, low, high):
  """Return True if target is found in indicated portion of a Python list.

  The search only considers the portion from data[low] to data[high] inclusive.
  """
  if low > high:
    return False                    # interval is empty; no match
  else:
    mid = (low + high) // 2
    if target == data[mid]:         # found a match
      return True
    elif target < data[mid]:
      # recur on the portion left of the middle
      return binary_search(data, target, low, mid - 1)
    else:
      # recur on the portion right of the middle
      return binary_search(data, target, mid + 1, high)
'''

### 4.1.4 - File System
'''
import os

def disk_usage(path):
  """Return the number of bytes used by a file/folder and any descendents."""
  total = os.path.getsize(path)                  # account for direct usage
  if os.path.isdir(path):                        # if this is a directory,
    for filename in os.listdir(path):            # then for each child:
      childpath = os.path.join(path, filename)   # compose full path to child
      total += disk_usage(childpath)             # add child's usage to total

  print ('{0:<7}'.format(total), path)           # descriptive output (optional)
  return total                                   # return the grand total
'''