from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# full specifications for tasks at https://docs.crewai.com/core-concepts/Tasks/

class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
            Description to LLM employee, describing the task to be complete.
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
    
            Use this variable: {var1}
            And also this variable: {var2}
        """
            ),
            
            expected_output=dedent("""
            Describe the output desired, eg text layout, JSON etc.
								"""),
            agent=agent,
        )

    def task_2_name(self, agent):
        return Task(
            description=dedent(
                f"""
            If not asynchronous, take the input from task 1 and do something with it.
                                       
            {self.__tip_section()}

            Make sure to do something else.
        """
            ),

            expected_output=dedent("""
            Describe the output desired, eg text layout, JSON etc.
								"""),
            agent=agent,
        )
