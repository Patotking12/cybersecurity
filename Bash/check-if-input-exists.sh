#! /bin/bash
read -p 'username: ' username
read -p 'group: ' groupname

if !(grep -q $username /etc/passwd) &&!(grep -q $groupname /etc/group)
then
   echo "Both are not found - why are you even asking me this?"

elif !(grep -q $username /etc/passwd) ||!(grep -q $groupname /etc/group)
then 
   echo "One exists, one does not. You figure out which."

else
   tmp=$(groups | grep -q $groupname)
   if [ -z "$tmp" ]
   then
          echo "Membership invalid but available to join"
   else
          echo "Membership valid!"
   fi
fi