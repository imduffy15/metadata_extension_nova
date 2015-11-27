
import setuptools

setuptools.setup(
    name="metadata_extension_nova",
    long_description="nova hooks to run on create_instance and delete_instance",
    author='Ian Duffy',
    author_email='ian@ianduffy.ie',
    zip_safe=False,
    version=1,
    packages=['metadata_extension_nova'],
    entry_points={
        'nova.hooks': [
            'create_instance=metadata_extension_nova.hook:HookCreate',
            'delete_instance=metadata_extension_nova.hook:HookDelete',
        ]
    },
)
