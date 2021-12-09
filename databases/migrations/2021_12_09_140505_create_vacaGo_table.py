"""CreateVacaGoTable Migration."""

from masoniteorm.migrations import Migration


class CreateVacaGoTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("vacaGo") as table:
            table.increments("id")
            table.string("city")
            table.string("activity")
            table.string("details")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("vacaGo")
