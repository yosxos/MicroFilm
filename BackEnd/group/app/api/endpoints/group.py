from api.models.group_model import GroupOut,GroupIn
from fastapi import APIRouter, Depends, HTTPException, status
from databases import Database


DATABASE_URL = 'postgresql://postgres:198650@localhost/movie_app_db'
database=Database(DATABASE_URL)

router = APIRouter(
    prefix="/group",
    tags=["group"],
)

@router.get("/{group_id}",response_model=GroupOut)
async def get_user(group_id: int):
    """
    Get a group by id

    Args:
        group_id (int): The id of the group

    Returns:
        GroupOut: The group with the given id
    """
    query = """SELECT * FROM "group" WHERE id = :group_id"""
    values = {"group_id": group_id}
    group = await database.fetch_one(query=query, values=values)
    return group

@router.post("/create")
async def create_group(group: GroupIn):
    """
    Create a new group

    """
    query = """INSERT INTO "group" (name) VALUES (:name);"""
    values = {"name": group.name}
    await database.execute(query=query, values=values)
    return "Group created"

@router.put("/update/{group_id}")
async def update_group(group_id: int, group: GroupIn):
    query="""UPDATE "group" SET name=:name WHERE id=:group_id"""
    values={"name": group.name, "group_id": group_id}
    await database.execute(query=query, values=values)
    return "Group updated"

@router.delete("/delete/{group_id}")
async def delete_group(group_id: int):
    """
    Delete a group by id

    Args:
        group_id (int):  The id of the group
    """
    query="""DELETE FROM "group" WHERE id=:group_id"""
    values={"group_id": group_id}
    await database.execute(query=query, values=values)
    return "Group deleted"

@router.get('/{group_id}/Users')
async def get_group_users(group_id: int):
    """
    Get all users of a group

    Args:
        group_id (int): group id
    """
    query="SELECT u.name,u.id FROM users u INNER JOIN user_group ug ON u.id=ug.user_id WHERE ug.group_id=:group_id"
    values={"group_id": group_id}
    users= await database.fetch_all(query=query, values=values)
    return users

# Cette requête est optionnelle car on a déjà un moyen d'ajouter un user à un group avec l'api "user"
@router.post('/{group_id}/Users/add')
async def add_user_group(user_id: int, group_id: int):
    """
    Add a user to a group

    Args:
        user_id (int): user id
        group_id (int): group id
    """
    query="INSERT INTO user_group (user_id, group_id) SELECT :user_id, :group_id WHERE NOT EXISTS (  SELECT 1  FROM user_group  WHERE user_id = :user_id AND group_id = :group_id)"
    values={"user_id": user_id, "group_id": group_id}
    await database.execute(query=query, values=values)
    return "User added"

@router.put('/{group_id}/Users/update/{user_id}')
async def update_group_user(user_id: int, group_id: int,user_update_id: int):
    """
    Update a user from a group

    Args:
        user_id (int): User id
        group_id (int): Group id
        user_update_id (int): User id to update

    """
    query="UPDATE user_group SET user_id=:user_update_id WHERE group_id=:group_id AND user_id=:user_id"
    values={"user_id": user_id, "group_id": group_id, "group_update_id": user_update_id}
    await database.execute(query=query, values=values)
    return "User updated"

@router.delete('/{group_id}/Groups/delete/{user_id}')
async def delete_group_user(user_id: int, group_id: int):
    """
    Delete a user from a group

    Args:
        user_id (int): user id
        group_id (int): group id
    """
    query="DELETE FROM user_group WHERE user_id=:user_id AND group_id=:group_id"
    values={"user_id": user_id, "group_id": group_id}
    await database.execute(query=query, values=values)
    return "User deleted"