"""Asana entity schemas."""

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from airweave.platform.entities._base import ChunkEntity, FileEntity


class AsanaWorkspaceEntity(ChunkEntity):
    """Schema for Asana workspace entities."""

    name: str = Field(..., description="The name of the workspace")
    asana_gid: str = Field(..., description="Globally unique identifier of the workspace")
    is_organization: bool = Field(False, description="Whether the workspace is an organization")
    email_domains: List[str] = Field(
        default_factory=list, description="List of email domains that can access this workspace"
    )
    permalink_url: Optional[str] = Field(
        None, description="URL to access the workspace in the Asana application"
    )


class AsanaProjectEntity(ChunkEntity):
    """Schema for Asana project entities."""

    name: str = Field(..., description="The name of the project")
    workspace_gid: str = Field(
        ..., description="Globally unique identifier of the workspace the project belongs to"
    )
    workspace_name: str = Field(..., description="The name of the workspace the project belongs to")
    color: Optional[str] = Field(
        None, description="Color of the project (e.g. 'dark-pink', 'light-blue')"
    )
    archived: bool = Field(False, description="Whether the project is archived")
    created_at: Optional[datetime] = Field(
        None, description="The time at which this project was created"
    )
    current_status: Optional[Dict] = Field(
        None, description="The current status update for this project"
    )
    default_view: Optional[str] = Field(
        None, description="The default view of the project (list, board, calendar, timeline)"
    )
    due_date: Optional[str] = Field(
        None, description="The day on which this project is due (YYYY-MM-DD format)"
    )
    due_on: Optional[str] = Field(
        None, description="The day on which this project is due (YYYY-MM-DD format)"
    )
    html_notes: Optional[str] = Field(
        None, description="HTML formatted note content of the project"
    )
    notes: Optional[str] = Field(
        None, description="Free-form textual information associated with the project"
    )
    is_public: bool = Field(False, description="Whether the project is public to its team")
    start_on: Optional[str] = Field(
        None, description="The day on which this project starts (YYYY-MM-DD format)"
    )
    modified_at: Optional[datetime] = Field(
        None, description="The time at which this project was last modified"
    )
    owner: Optional[Dict] = Field(None, description="The owner of this project")
    team: Optional[Dict] = Field(None, description="The team that this project is associated with")
    members: List[Dict] = Field(
        default_factory=list, description="Array of users who are members of this project"
    )
    followers: List[Dict] = Field(
        default_factory=list, description="Array of users following this project"
    )
    custom_fields: List[Dict] = Field(
        default_factory=list, description="Array of custom field values applied to the project"
    )
    custom_field_settings: List[Dict] = Field(
        default_factory=list, description="Array of custom field settings for this project"
    )
    default_access_level: Optional[str] = Field(
        None, description="Default access level for the project (editor, commenter, viewer)"
    )
    icon: Optional[str] = Field(None, description="The icon for a project")
    permalink_url: Optional[str] = Field(
        None, description="URL to access the project in the Asana application"
    )


class AsanaSectionEntity(ChunkEntity):
    """Schema for Asana section entities."""

    name: str = Field(..., description="The name of the section")
    project_gid: str = Field(
        ..., description="Globally unique identifier of the project this section belongs to"
    )
    created_at: Optional[datetime] = Field(
        None, description="The time at which this section was created"
    )
    projects: List[Dict] = Field(
        default_factory=list,
        description="Deprecated. Array of projects this section is associated with",
    )


class AsanaTaskEntity(ChunkEntity):
    """Schema for Asana task entities."""

    name: str = Field(..., description="The name of the task")
    project_gid: str = Field(
        ..., description="Globally unique identifier of the project this task belongs to"
    )
    section_gid: Optional[str] = Field(
        None, description="Globally unique identifier of the section this task belongs to"
    )
    actual_time_minutes: Optional[int] = Field(
        None, description="The actual time spent on this task in minutes"
    )
    approval_status: Optional[str] = Field(
        None, description="The status of the task's approval, if applicable"
    )
    assignee: Optional[Dict] = Field(None, description="User to which this task is assigned")
    assignee_status: Optional[str] = Field(
        None, description="The scheduling status of this task for the user it's assigned to"
    )
    completed: bool = Field(False, description="Whether the task is marked complete")
    completed_at: Optional[datetime] = Field(
        None, description="The time at which this task was completed"
    )
    completed_by: Optional[Dict] = Field(None, description="The user who completed this task")
    created_at: Optional[datetime] = Field(
        None, description="The time at which this task was created"
    )
    dependencies: List[Dict] = Field(
        default_factory=list, description="Array of tasks that this task depends on"
    )
    dependents: List[Dict] = Field(
        default_factory=list, description="Array of tasks that depend on this task"
    )
    due_at: Optional[datetime] = Field(
        None, description="The time at which this task is due with a time component"
    )
    due_on: Optional[str] = Field(
        None, description="The date on which this task is due (YYYY-MM-DD format)"
    )
    external: Optional[Dict] = Field(
        None, description="Information about the external application syncing with this task"
    )
    html_notes: Optional[str] = Field(None, description="HTML formatted note content of the task")
    notes: Optional[str] = Field(
        None, description="Free-form textual information associated with the task"
    )
    is_rendered_as_separator: bool = Field(
        False, description="Whether the task is rendered as a separator in list view"
    )
    liked: bool = Field(False, description="Whether the task is liked by the authorized user")
    memberships: List[Dict] = Field(
        default_factory=list, description="Array of projects and sections this task is in"
    )
    modified_at: Optional[datetime] = Field(
        None, description="The time at which this task was last modified"
    )
    num_likes: int = Field(0, description="The number of users who have liked this task")
    num_subtasks: int = Field(0, description="The number of subtasks on this task")
    parent: Optional[Dict] = Field(None, description="The parent of this task, if applicable")
    permalink_url: Optional[str] = Field(
        None, description="URL to access the task in the Asana application"
    )
    resource_subtype: str = Field(
        "default_task", description="The subtype of the task (default_task, milestone, approval)"
    )
    start_at: Optional[datetime] = Field(
        None, description="The time at which this task starts with a time component"
    )
    start_on: Optional[str] = Field(
        None, description="The date on which this task starts (YYYY-MM-DD format)"
    )
    tags: List[Dict] = Field(
        default_factory=list, description="Array of tags associated with this task"
    )
    custom_fields: List[Dict] = Field(
        default_factory=list, description="Array of custom field values applied to the task"
    )
    followers: List[Dict] = Field(
        default_factory=list, description="Array of users following this task"
    )
    workspace: Optional[Dict] = Field(
        None, description="The workspace this task is associated with"
    )


class AsanaCommentEntity(ChunkEntity):
    """Schema for Asana comment/story entities."""

    task_gid: str = Field(
        ..., description="Globally unique identifier of the task this comment belongs to"
    )
    author: Dict = Field(..., description="The user who created this comment")
    created_at: datetime = Field(..., description="The time at which this comment was created")
    resource_subtype: str = Field(
        "comment_added", description="The subtype of the comment resource"
    )
    text: Optional[str] = Field(None, description="The plain text content of the comment")
    html_text: Optional[str] = Field(None, description="HTML formatted content of the comment")
    is_pinned: bool = Field(False, description="Whether the comment is pinned to the task")
    is_edited: bool = Field(False, description="Whether the comment has been edited")
    sticker_name: Optional[str] = Field(
        None, description="The name of the sticker (for sticker comments)"
    )
    num_likes: int = Field(0, description="The number of users who have liked this comment")
    liked: bool = Field(False, description="Whether the comment is liked by the authorized user")
    type: str = Field("comment", description="The type of the comment (comment or system)")
    previews: List[Dict] = Field(
        default_factory=list, description="Previews of attachments referenced in the comment"
    )


class AsanaFileEntity(FileEntity):
    """Schema for Asana file attachments.

    Reference:
        https://developers.asana.com/reference/getattachment
    """

    task_gid: str = Field(..., description="GID of the task this file is attached to")
    task_name: str = Field(..., description="Name of the task this file is attached to")
    resource_type: str = Field(..., description="Type of the attachment resource")
    host: Optional[str] = Field(None, description="Service hosting the attachment")
    parent: Optional[Dict[str, Any]] = Field(
        None, description="Parent resource the attachment is on"
    )
    view_url: Optional[str] = Field(None, description="URL to view the attachment")
    permanent: bool = Field(False, description="Whether this is a permanent attachment")
