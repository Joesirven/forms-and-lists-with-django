# Generated by Django 4.1.2 on 2022-10-13 11:41

from django.db import migrations


def make_posts(apps, schema):
    Post = apps.get_model("posts", "Post")
    Post.objects.create(
        title="My first post!",
        summary="This is my first post",
        content="""
        Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Vestibulum elementum ut augue eu ultrices.
        Nullam vehicula sem nisi, ut laoreet tortor faucibus
        sed. Morbi faucibus tincidunt velit quis posuere.
        Donec nisl lacus, pulvinar et elementum ut,
        ullamcorper id tortor. Morbi sodales erat et purus
        vestibulum, vitae sodales risus sollicitudin. Ut
        facilisis, urna a vulputate lacinia, mi justo mollis
        justo, ac iaculis neque nisl non nunc. Nullam
        vulputate turpis id efficitur posuere. Nullam quis
        tristique erat. Nunc maximus congue nisi, quis
        laoreet nisl pellentesque vel. Curabitur congue eu
        libero molestie elementum.
        """,
    )
    Post.objects.create(
        title="My second post!",
        summary="You're still here? Thanks!",
        content="""
        Aenean congue ex sed est sagittis ornare. Morbi sit
        amet metus finibus, cursus lacus tempor, tincidunt
        sem. Nullam aliquet justo id libero porttitor, vitae
        consequat leo malesuada. Proin suscipit eleifend mi
        et rutrum. Donec vulputate gravida ligula vel
        tempus. Aliquam dolor nisi, pretium non accumsan
        vel, ornare ac erat. Proin ultricies dignissim
        sapien, quis consectetur erat sagittis a. Sed
        convallis nunc mauris, quis porttitor purus eleifend
        et. Nullam lobortis ac tortor non sodales. Nullam
        aliquam finibus laoreet. Donec interdum metus at
        convallis facilisis. Pellentesque a felis ipsum.
        Phasellus dolor tellus, ornare a maximus eu, rutrum
        a libero. Nam a imperdiet ex, non pulvinar lorem.
        Integer nec lacus lacinia, ultrices sapien non,
        mollis tortor.
        """
    )


def remove_posts(apps, schema):
    Post = apps.get_model("posts", "Post")
    Post.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(make_posts, remove_posts)
    ]