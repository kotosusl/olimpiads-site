import { defineStore } from 'pinia'

const UserList0 = defineStore('UserList', {
    state: () => ({
       users: [
          {
             name: 'Alex'
          },
          {
             name: 'Vasya'
          }
       ]
    }),
 
    getters: {
       Users: (state) => state.users,
    },
 
    actions: {
       Append(n)
       {
          this.users.push({
             name: n,
          })
       }
    }
 })

const UserList = defineStore('UserList', {
    state: () => ({
       users: [
          {
             user_id: 1,
             name: 'username',
             surname: 'usersurname',
             male: 'F',
             school_class: 10,
             subjects: ['Math', 'Physics'],
             messages_places: ['Telegram', 'Mail']
          }
       ]
    }),
    getters: {
       Users: (state) => state.users,
    }
 })

 export { UserList }