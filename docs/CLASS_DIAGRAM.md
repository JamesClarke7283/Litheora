```mermaid
classDiagram
    class Permission {
    +String title
}
    class Role {
    +String title
    +List[Permission] permission
    }

    class User {
    +String username
    +String hashed_password
    +Dictionary attributes
    +Role role
    }
    Role "1" -- "0..*" Permission
    User "1" -- "1" Role

    class Site {
    +String title
    +String description
    +String host
    +String db_string
    +Permission create_page
    +Role default_user_role
    }
    Site "1" -- "0..*" User
    Site "1" -- "1" Permission
    Site "1" -- "1" Role

    class Page {
        +String url
        +Dictionary attributes
        +List[Block] blocks
        +Permission view
        +Permission edit
        +Permission delete
    }
    Page "1" -- "1" Permission
    Page "1" -- "0..*" Block

    class BlockType {
        +Tile tile
        +String template_path
    }    
    class Block {
        +BlockType type
        +Dictionary attributes
        +List[Block] inner_blocks
    }
    BlockType "1" -- "0..*" Block
    Block "1" -- "0..*" Block
    BlockType "1" -- "1" Tile

    class Image {
        +String title
        +String path
    }
    class Tile {
        +String title
        +Image icon
        +String url
    }
    Tile "1" -- "0..1" Image

```