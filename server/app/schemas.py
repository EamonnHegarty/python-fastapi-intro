from pydantic import BaseModel


# like typescript giving it a type
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
