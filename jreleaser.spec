# Generated with JReleaser 1.0.0-SNAPSHOT at 2022-02-13T12:11:01.494659Z
Name:      jreleaser
Version:   1.0.0~M2
Release:   1%{?dist}
Summary:   Release projects quickly and easily with JReleaser

License:   Apache-2.0
URL:       https://jreleaser.org
Source0:   https://github.com/jreleaser/jreleaser/releases/download/v1.0.0-M2/jreleaser-1.0.0-M2.tar

BuildArch: noarch
Requires:  java

%description
JReleaser is a release automation tool. Its goal is to simplify creating releases and
publishing artifacts to multiple package managers while providing customizable options.

JReleaser takes inputs from popular builds tools (Ant, Maven, Gradle) such as JAR files,
binary distributions (.zip, .tar), JLink images, or any other file that you’d like to
publish as a Git release on popular Git services such as GitHub, GitLab, or Gitea.
Distribution files may additionally be published to be consumed by popular package managers
such as Homebrew, Chocolatey, Snapcraft, or get ready to be launched via JBang. Releases
may be announced in a variety of channels such as Twitter, Zulip, SDKMAN!, and more.


%prep
%setup -q -n jreleaser-1.0.0-M2

%install
mkdir -p %{buildroot}%{_bindir}
%define _appdir %{buildroot}%{_datadir}/%{name}
mkdir -p %{_appdir}/bin

cat > %{buildroot}%{_bindir}/jreleaser <<-EOF
#!/bin/sh
%{_datadir}/%{name}/bin/jreleaser "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/jreleaser

mkdir -p %{_appdir}/lib
install -p -m 755 bin/jreleaser %{_appdir}/bin/jreleaser
install -p -m 644 VERSION %{_appdir}/VERSION
install -p -m 644 lib/JavaEWAH-1.1.12.jar %{_appdir}/lib/JavaEWAH-1.1.12.jar
install -p -m 644 lib/artifactory-java-sdk-1.0.0-M2.jar %{_appdir}/lib/artifactory-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/aws-java-sdk-core-1.12.143.jar %{_appdir}/lib/aws-java-sdk-core-1.12.143.jar
install -p -m 644 lib/aws-java-sdk-kms-1.12.143.jar %{_appdir}/lib/aws-java-sdk-kms-1.12.143.jar
install -p -m 644 lib/aws-java-sdk-s3-1.12.143.jar %{_appdir}/lib/aws-java-sdk-s3-1.12.143.jar
install -p -m 644 lib/bcpg-jdk15on-1.68.jar %{_appdir}/lib/bcpg-jdk15on-1.68.jar
install -p -m 644 lib/bcprov-jdk15on-1.68.jar %{_appdir}/lib/bcprov-jdk15on-1.68.jar
install -p -m 644 lib/classmate-1.5.1.jar %{_appdir}/lib/classmate-1.5.1.jar
install -p -m 644 lib/codeberg-java-sdk-1.0.0-M2.jar %{_appdir}/lib/codeberg-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/commons-codec-1.15.jar %{_appdir}/lib/commons-codec-1.15.jar
install -p -m 644 lib/commons-compress-1.21.jar %{_appdir}/lib/commons-compress-1.21.jar
install -p -m 644 lib/commons-io-2.11.0.jar %{_appdir}/lib/commons-io-2.11.0.jar
install -p -m 644 lib/commons-lang3-3.12.0.jar %{_appdir}/lib/commons-lang3-3.12.0.jar
install -p -m 644 lib/compiler-0.9.10.jar %{_appdir}/lib/compiler-0.9.10.jar
install -p -m 644 lib/discord-java-sdk-1.0.0-M2.jar %{_appdir}/lib/discord-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/feign-core-11.8.jar %{_appdir}/lib/feign-core-11.8.jar
install -p -m 644 lib/feign-form-3.8.0.jar %{_appdir}/lib/feign-form-3.8.0.jar
install -p -m 644 lib/feign-httpclient-11.8.jar %{_appdir}/lib/feign-httpclient-11.8.jar
install -p -m 644 lib/feign-jackson-11.8.jar %{_appdir}/lib/feign-jackson-11.8.jar
install -p -m 644 lib/genericgit-java-sdk-1.0.0-M2.jar %{_appdir}/lib/genericgit-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/git-sdk-1.0.0-M2.jar %{_appdir}/lib/git-sdk-1.0.0-M2.jar
install -p -m 644 lib/gitea-java-sdk-1.0.0-M2.jar %{_appdir}/lib/gitea-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/github-api-1.129.jar %{_appdir}/lib/github-api-1.129.jar
install -p -m 644 lib/github-java-sdk-1.0.0-M2.jar %{_appdir}/lib/github-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/gitlab-java-sdk-1.0.0-M2.jar %{_appdir}/lib/gitlab-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/gitter-java-sdk-1.0.0-M2.jar %{_appdir}/lib/gitter-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/google-chat-java-sdk-1.0.0-M2.jar %{_appdir}/lib/google-chat-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/http-upload-java-sdk-1.0.0-M2.jar %{_appdir}/lib/http-upload-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/httpclient-4.5.13.jar %{_appdir}/lib/httpclient-4.5.13.jar
install -p -m 644 lib/httpcore-4.4.13.jar %{_appdir}/lib/httpcore-4.4.13.jar
install -p -m 644 lib/ion-java-1.0.2.jar %{_appdir}/lib/ion-java-1.0.2.jar
install -p -m 644 lib/jackson-annotations-2.13.1.jar %{_appdir}/lib/jackson-annotations-2.13.1.jar
install -p -m 644 lib/jackson-core-2.13.1.jar %{_appdir}/lib/jackson-core-2.13.1.jar
install -p -m 644 lib/jackson-databind-2.13.1.jar %{_appdir}/lib/jackson-databind-2.13.1.jar
install -p -m 644 lib/jackson-dataformat-cbor-2.13.1.jar %{_appdir}/lib/jackson-dataformat-cbor-2.13.1.jar
install -p -m 644 lib/jackson-dataformat-toml-2.13.1.jar %{_appdir}/lib/jackson-dataformat-toml-2.13.1.jar
install -p -m 644 lib/jackson-dataformat-yaml-2.13.1.jar %{_appdir}/lib/jackson-dataformat-yaml-2.13.1.jar
install -p -m 644 lib/jakarta.activation-2.0.1.jar %{_appdir}/lib/jakarta.activation-2.0.1.jar
install -p -m 644 lib/jakarta.mail-2.0.1.jar %{_appdir}/lib/jakarta.mail-2.0.1.jar
install -p -m 644 lib/java-sdk-commons-1.0.0-M2.jar %{_appdir}/lib/java-sdk-commons-1.0.0-M2.jar
install -p -m 644 lib/jcl-over-slf4j-1.7.33.jar %{_appdir}/lib/jcl-over-slf4j-1.7.33.jar
install -p -m 644 lib/jmespath-java-1.12.143.jar %{_appdir}/lib/jmespath-java-1.12.143.jar
install -p -m 644 lib/joda-time-2.8.1.jar %{_appdir}/lib/joda-time-2.8.1.jar
install -p -m 644 lib/jreleaser-1.0.0-M2.jar %{_appdir}/lib/jreleaser-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-assemblers-1.0.0-M2.jar %{_appdir}/lib/jreleaser-assemblers-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-config-json-1.0.0-M2.jar %{_appdir}/lib/jreleaser-config-json-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-config-toml-1.0.0-M2.jar %{_appdir}/lib/jreleaser-config-toml-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-config-yaml-1.0.0-M2.jar %{_appdir}/lib/jreleaser-config-yaml-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-engine-1.0.0-M2.jar %{_appdir}/lib/jreleaser-engine-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-model-1.0.0-M2.jar %{_appdir}/lib/jreleaser-model-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-templates-1.0.0-M2.jar %{_appdir}/lib/jreleaser-templates-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-tools-1.0.0-M2.jar %{_appdir}/lib/jreleaser-tools-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-utils-1.0.0-M2.jar %{_appdir}/lib/jreleaser-utils-1.0.0-M2.jar
install -p -m 644 lib/jreleaser-workflow-1.0.0-M2.jar %{_appdir}/lib/jreleaser-workflow-1.0.0-M2.jar
install -p -m 644 lib/jsonschema-generator-4.22.0.jar %{_appdir}/lib/jsonschema-generator-4.22.0.jar
install -p -m 644 lib/jsonschema-module-jackson-4.22.0.jar %{_appdir}/lib/jsonschema-module-jackson-4.22.0.jar
install -p -m 644 lib/mail-java-sdk-1.0.0-M2.jar %{_appdir}/lib/mail-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/mastodon-java-sdk-1.0.0-M2.jar %{_appdir}/lib/mastodon-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/mattermost-java-sdk-1.0.0-M2.jar %{_appdir}/lib/mattermost-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/org.eclipse.jgit-5.13.0.202109080827-r.jar %{_appdir}/lib/org.eclipse.jgit-5.13.0.202109080827-r.jar
install -p -m 644 lib/org.tukaani.xz-0.3.jar %{_appdir}/lib/org.tukaani.xz-0.3.jar
install -p -m 644 lib/os-maven-plugin-1.7.0.jar %{_appdir}/lib/os-maven-plugin-1.7.0.jar
install -p -m 644 lib/picocli-4.6.2.jar %{_appdir}/lib/picocli-4.6.2.jar
install -p -m 644 lib/s3-java-sdk-1.0.0-M2.jar %{_appdir}/lib/s3-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/sdkman-java-sdk-1.0.0-M2.jar %{_appdir}/lib/sdkman-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/slack-java-sdk-1.0.0-M2.jar %{_appdir}/lib/slack-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/slf4j-api-1.7.33.jar %{_appdir}/lib/slf4j-api-1.7.33.jar
install -p -m 644 lib/slf4j-simple-1.7.33.jar %{_appdir}/lib/slf4j-simple-1.7.33.jar
install -p -m 644 lib/snakeyaml-1.30.jar %{_appdir}/lib/snakeyaml-1.30.jar
install -p -m 644 lib/teams-java-sdk-1.0.0-M2.jar %{_appdir}/lib/teams-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/telegram-java-sdk-1.0.0-M2.jar %{_appdir}/lib/telegram-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/tika-core-2.2.1.jar %{_appdir}/lib/tika-core-2.2.1.jar
install -p -m 644 lib/tool-sdk-1.0.0-M2.jar %{_appdir}/lib/tool-sdk-1.0.0-M2.jar
install -p -m 644 lib/twitter-java-sdk-1.0.0-M2.jar %{_appdir}/lib/twitter-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/twitter4j-core-4.0.7.jar %{_appdir}/lib/twitter4j-core-4.0.7.jar
install -p -m 644 lib/webhooks-java-sdk-1.0.0-M2.jar %{_appdir}/lib/webhooks-java-sdk-1.0.0-M2.jar
install -p -m 644 lib/yamllint-1.5.0.jar %{_appdir}/lib/yamllint-1.5.0.jar
install -p -m 644 lib/zt-exec-1.12.jar %{_appdir}/lib/zt-exec-1.12.jar
install -p -m 644 lib/zulip-java-sdk-1.0.0-M2.jar %{_appdir}/lib/zulip-java-sdk-1.0.0-M2.jar

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/bin/jreleaser
%{_datadir}/%{name}/VERSION
%{_datadir}/%{name}/lib/JavaEWAH-1.1.12.jar
%{_datadir}/%{name}/lib/artifactory-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/aws-java-sdk-core-1.12.143.jar
%{_datadir}/%{name}/lib/aws-java-sdk-kms-1.12.143.jar
%{_datadir}/%{name}/lib/aws-java-sdk-s3-1.12.143.jar
%{_datadir}/%{name}/lib/bcpg-jdk15on-1.68.jar
%{_datadir}/%{name}/lib/bcprov-jdk15on-1.68.jar
%{_datadir}/%{name}/lib/classmate-1.5.1.jar
%{_datadir}/%{name}/lib/codeberg-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/commons-codec-1.15.jar
%{_datadir}/%{name}/lib/commons-compress-1.21.jar
%{_datadir}/%{name}/lib/commons-io-2.11.0.jar
%{_datadir}/%{name}/lib/commons-lang3-3.12.0.jar
%{_datadir}/%{name}/lib/compiler-0.9.10.jar
%{_datadir}/%{name}/lib/discord-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/feign-core-11.8.jar
%{_datadir}/%{name}/lib/feign-form-3.8.0.jar
%{_datadir}/%{name}/lib/feign-httpclient-11.8.jar
%{_datadir}/%{name}/lib/feign-jackson-11.8.jar
%{_datadir}/%{name}/lib/genericgit-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/git-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/gitea-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/github-api-1.129.jar
%{_datadir}/%{name}/lib/github-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/gitlab-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/gitter-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/google-chat-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/http-upload-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/httpclient-4.5.13.jar
%{_datadir}/%{name}/lib/httpcore-4.4.13.jar
%{_datadir}/%{name}/lib/ion-java-1.0.2.jar
%{_datadir}/%{name}/lib/jackson-annotations-2.13.1.jar
%{_datadir}/%{name}/lib/jackson-core-2.13.1.jar
%{_datadir}/%{name}/lib/jackson-databind-2.13.1.jar
%{_datadir}/%{name}/lib/jackson-dataformat-cbor-2.13.1.jar
%{_datadir}/%{name}/lib/jackson-dataformat-toml-2.13.1.jar
%{_datadir}/%{name}/lib/jackson-dataformat-yaml-2.13.1.jar
%{_datadir}/%{name}/lib/jakarta.activation-2.0.1.jar
%{_datadir}/%{name}/lib/jakarta.mail-2.0.1.jar
%{_datadir}/%{name}/lib/java-sdk-commons-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jcl-over-slf4j-1.7.33.jar
%{_datadir}/%{name}/lib/jmespath-java-1.12.143.jar
%{_datadir}/%{name}/lib/joda-time-2.8.1.jar
%{_datadir}/%{name}/lib/jreleaser-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-assemblers-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-config-json-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-config-toml-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-config-yaml-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-engine-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-model-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-templates-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-tools-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-utils-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jreleaser-workflow-1.0.0-M2.jar
%{_datadir}/%{name}/lib/jsonschema-generator-4.22.0.jar
%{_datadir}/%{name}/lib/jsonschema-module-jackson-4.22.0.jar
%{_datadir}/%{name}/lib/mail-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/mastodon-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/mattermost-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/org.eclipse.jgit-5.13.0.202109080827-r.jar
%{_datadir}/%{name}/lib/org.tukaani.xz-0.3.jar
%{_datadir}/%{name}/lib/os-maven-plugin-1.7.0.jar
%{_datadir}/%{name}/lib/picocli-4.6.2.jar
%{_datadir}/%{name}/lib/s3-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/sdkman-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/slack-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/slf4j-api-1.7.33.jar
%{_datadir}/%{name}/lib/slf4j-simple-1.7.33.jar
%{_datadir}/%{name}/lib/snakeyaml-1.30.jar
%{_datadir}/%{name}/lib/teams-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/telegram-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/tika-core-2.2.1.jar
%{_datadir}/%{name}/lib/tool-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/twitter-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/twitter4j-core-4.0.7.jar
%{_datadir}/%{name}/lib/webhooks-java-sdk-1.0.0-M2.jar
%{_datadir}/%{name}/lib/yamllint-1.5.0.jar
%{_datadir}/%{name}/lib/zt-exec-1.12.jar
%{_datadir}/%{name}/lib/zulip-java-sdk-1.0.0-M2.jar
