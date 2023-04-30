import { Component, OnInit } from '@angular/core';
import { Group } from '../../models/group';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {

  groups: Group[] = [];
  selectedGroup: Group = <Group>{};

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    this.getGroups();
  }
  getGroups() {
    this.userService.getUserGroups().subscribe((groups: Group[]) => {
        this.groups = groups;
    });
}

addGroup(name: string) {
    const group: Group = {id: 0, name};
    this.userService.addUserGroup(group).subscribe((addedGroup: Group) => {
        this.groups.push(addedGroup);
        this.clearForm();
    });
}

updateGroup() {
    this.userService.updateUserGroup(this.selectedGroup, this.selectedGroup).subscribe((updatedGroup: Group) => {
        const groupIndex = this.groups.findIndex(group => group.id === updatedGroup.id);
        if (groupIndex >= 0) {
            this.groups[groupIndex] = updatedGroup;
        }
        this.selectedGroup = <Group>{};
    });
}

deleteGroup() {
    this.userService.deleteUserGroup(this.selectedGroup).subscribe(() => {
        this.groups = this.groups.filter(group => group.id !== this.selectedGroup.id);
        this.selectedGroup = <Group>{};
    });
}

/*
  getGroups() {
    this.userService.getUserGroups().subscribe((groups: Group[]) => {
      this.groups = groups;
    });
  }

  addGroup(name: string) {
    const group: Group = {id: 0, name};
    this.userService.addUserGroup(group).subscribe((addedGroup: Group) => {
      this.groups.push(addedGroup);
      this.clearForm();
    });
  }

  updateGroup() {
    this.userService.updateUserGroup(this.selectedGroup, this.selectedGroup).subscribe((updatedGroup: Group) => {
      const groupIndex = this.groups.findIndex(group => group.id === updatedGroup.id);
      if (groupIndex >= 0) {
        this.groups[groupIndex] = updatedGroup;
      }
      this.selectedGroup = <Group>{};
    });
  }

  deleteGroup() {
    this.userService.deleteUserGroup(this.selectedGroup).subscribe(() => {
      this.groups = this.groups.filter(group => group.id !== this.selectedGroup.id);
      this.selectedGroup = <Group>{};
    });
  }
*/
  clearForm() {
    this.selectedGroup = <Group>{};
    
  }

}
