## Assignment 1 - VM and RAID1
### What is RAID:
https://en.wikipedia.org/wiki/RAID

### Steps
1. Create Virtual Machine with Debian/Ubuntu/CentOS or download preinstalled image (https://www.osboxes.org/).
2. Add simple RAID1 to Virtual Machine:
*nix OS System on 1-st HDD, 2d and 3d HDDs are in RAID1.
2 (with star). only two HDDs. OS System on RAID1, based on this two HDD.
3. How to test RAID1. Create file on RAID1 file system. Turn off VM and remove one of the HHDs from VM. Turn on VM. File should be accessible.
4. Add new HDD and sync it to RAID1.
5. Add section with Assignment1 description into docx and send by e-mail for checking.

### Instruction examples:

- https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu-16-04
- (How to remove disk from RAID1) https://unix.stackexchange.com/questions/332061/remove-drive-from-soft-raid
