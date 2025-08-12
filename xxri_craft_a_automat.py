import os
import json

class AutomatedDevOpsPipelineAnalyzer:
    def __init__(self, pipeline_config):
        self.pipeline_config = pipeline_config

    def analyze_pipeline(self):
        pipeline_stages = self.pipeline_config['stages']
        issues = []

        for stage in pipeline_stages:
            if 'script' in stage:
                script_path = stage['script']
                if not os.path.exists(script_path):
                    issues.append(f"Script '{script_path}' not found")

            if 'dependencies' in stage:
                dependencies = stage['dependencies']
                for dependency in dependencies:
                    if 'version' not in dependency:
                        issues.append(f"Dependency '{dependency['name']}' missing version")

        return issues

def test_automated_devops_pipeline_analyzer():
    pipeline_config = {
        'stages': [
            {
                'name': 'build',
                'script': 'build_script.sh',
                'dependencies': [
                    {'name': 'java', 'version': '1.8'},
                    {'name': 'maven'}
                ]
            },
            {
                'name': 'deploy',
                'script': 'deploy_script.sh',
                'dependencies': [
                    {'name': 'kubernetes', 'version': '1.21'}
                ]
            }
        ]
    }

    analyzer = AutomatedDevOpsPipelineAnalyzer(pipeline_config)
    issues = analyzer.analyze_pipeline()

    if len(issues) > 0:
        print("Pipeline issues:")
        for issue in issues:
            print(issue)
    else:
        print("Pipeline is healthy")

if __name__ == "__main__":
    test_automated_devops_pipeline_analyzer()