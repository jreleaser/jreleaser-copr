# Generated with JReleaser 1.4.0-SNAPSHOT at 2022-12-29T16:04:33.910943262Z
Name:      jreleaser
Version:   1.4.0
Release:   1%{?dist}
Summary:   Release projects quickly and easily with JReleaser

License:   Apache-2.0
URL:       https://jreleaser.org
Source0:   https://github.com/jreleaser/jreleaser/releases/download/v1.4.0/jreleaser-1.4.0.tar

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
%setup -q -n jreleaser-1.4.0

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
install -p -m 644 lib/asn-one-0.6.0.jar %{_appdir}/lib/asn-one-0.6.0.jar
install -p -m 644 lib/aws-java-sdk-core-1.12.326.jar %{_appdir}/lib/aws-java-sdk-core-1.12.326.jar
install -p -m 644 lib/aws-java-sdk-kms-1.12.326.jar %{_appdir}/lib/aws-java-sdk-kms-1.12.326.jar
install -p -m 644 lib/aws-java-sdk-s3-1.12.326.jar %{_appdir}/lib/aws-java-sdk-s3-1.12.326.jar
install -p -m 644 lib/bcpg-jdk15on-1.69.jar %{_appdir}/lib/bcpg-jdk15on-1.69.jar
install -p -m 644 lib/bcpkix-jdk15on-1.69.jar %{_appdir}/lib/bcpkix-jdk15on-1.69.jar
install -p -m 644 lib/bcprov-jdk15on-1.69.jar %{_appdir}/lib/bcprov-jdk15on-1.69.jar
install -p -m 644 lib/bcutil-jdk15on-1.69.jar %{_appdir}/lib/bcutil-jdk15on-1.69.jar
install -p -m 644 lib/classmate-1.5.1.jar %{_appdir}/lib/classmate-1.5.1.jar
install -p -m 644 lib/commonmark-0.21.0.jar %{_appdir}/lib/commonmark-0.21.0.jar
install -p -m 644 lib/commons-codec-1.15.jar %{_appdir}/lib/commons-codec-1.15.jar
install -p -m 644 lib/commons-compress-1.21.jar %{_appdir}/lib/commons-compress-1.21.jar
install -p -m 644 lib/commons-io-2.11.0.jar %{_appdir}/lib/commons-io-2.11.0.jar
install -p -m 644 lib/commons-lang3-3.12.0.jar %{_appdir}/lib/commons-lang3-3.12.0.jar
install -p -m 644 lib/commons-net-3.8.0.jar %{_appdir}/lib/commons-net-3.8.0.jar
install -p -m 644 lib/commons-text-1.10.0.jar %{_appdir}/lib/commons-text-1.10.0.jar
install -p -m 644 lib/compiler-0.9.10.jar %{_appdir}/lib/compiler-0.9.10.jar
install -p -m 644 lib/eddsa-0.3.0.jar %{_appdir}/lib/eddsa-0.3.0.jar
install -p -m 644 lib/failsafe-2.4.4.jar %{_appdir}/lib/failsafe-2.4.4.jar
install -p -m 644 lib/feign-core-12.1.jar %{_appdir}/lib/feign-core-12.1.jar
install -p -m 644 lib/feign-form-3.8.0.jar %{_appdir}/lib/feign-form-3.8.0.jar
install -p -m 644 lib/feign-httpclient-12.1.jar %{_appdir}/lib/feign-httpclient-12.1.jar
install -p -m 644 lib/feign-jackson-12.1.jar %{_appdir}/lib/feign-jackson-12.1.jar
install -p -m 644 lib/github-api-1.129.jar %{_appdir}/lib/github-api-1.129.jar
install -p -m 644 lib/httpclient-4.5.13.jar %{_appdir}/lib/httpclient-4.5.13.jar
install -p -m 644 lib/httpcore-4.4.13.jar %{_appdir}/lib/httpcore-4.4.13.jar
install -p -m 644 lib/ion-java-1.0.2.jar %{_appdir}/lib/ion-java-1.0.2.jar
install -p -m 644 lib/jackson-annotations-2.14.1.jar %{_appdir}/lib/jackson-annotations-2.14.1.jar
install -p -m 644 lib/jackson-core-2.14.1.jar %{_appdir}/lib/jackson-core-2.14.1.jar
install -p -m 644 lib/jackson-databind-2.14.1.jar %{_appdir}/lib/jackson-databind-2.14.1.jar
install -p -m 644 lib/jackson-dataformat-cbor-2.14.1.jar %{_appdir}/lib/jackson-dataformat-cbor-2.14.1.jar
install -p -m 644 lib/jackson-dataformat-toml-2.14.1.jar %{_appdir}/lib/jackson-dataformat-toml-2.14.1.jar
install -p -m 644 lib/jackson-dataformat-xml-2.14.1.jar %{_appdir}/lib/jackson-dataformat-xml-2.14.1.jar
install -p -m 644 lib/jackson-dataformat-yaml-2.14.1.jar %{_appdir}/lib/jackson-dataformat-yaml-2.14.1.jar
install -p -m 644 lib/jakarta.activation-2.0.1.jar %{_appdir}/lib/jakarta.activation-2.0.1.jar
install -p -m 644 lib/jakarta.mail-2.0.1.jar %{_appdir}/lib/jakarta.mail-2.0.1.jar
install -p -m 644 lib/jcl-over-slf4j-2.0.6.jar %{_appdir}/lib/jcl-over-slf4j-2.0.6.jar
install -p -m 644 lib/jmespath-java-1.12.326.jar %{_appdir}/lib/jmespath-java-1.12.326.jar
install -p -m 644 lib/joda-time-2.8.1.jar %{_appdir}/lib/joda-time-2.8.1.jar
install -p -m 644 lib/jreleaser-1.4.0.jar %{_appdir}/lib/jreleaser-1.4.0.jar
install -p -m 644 lib/jreleaser-artifactory-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-artifactory-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-codeberg-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-codeberg-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-command-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-command-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-config-json-1.4.0.jar %{_appdir}/lib/jreleaser-config-json-1.4.0.jar
install -p -m 644 lib/jreleaser-config-toml-1.4.0.jar %{_appdir}/lib/jreleaser-config-toml-1.4.0.jar
install -p -m 644 lib/jreleaser-config-yaml-1.4.0.jar %{_appdir}/lib/jreleaser-config-yaml-1.4.0.jar
install -p -m 644 lib/jreleaser-discord-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-discord-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-discourse-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-discourse-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-engine-1.4.0.jar %{_appdir}/lib/jreleaser-engine-1.4.0.jar
install -p -m 644 lib/jreleaser-ftp-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-ftp-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-genericgit-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-genericgit-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-git-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-git-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-gitea-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-gitea-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-github-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-github-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-gitlab-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-gitlab-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-gitter-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-gitter-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-google-chat-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-google-chat-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-graalvm-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-graalvm-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-http-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-http-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-java-sdk-commons-1.4.0.jar %{_appdir}/lib/jreleaser-java-sdk-commons-1.4.0.jar
install -p -m 644 lib/jreleaser-logger-api-1.4.0.jar %{_appdir}/lib/jreleaser-logger-api-1.4.0.jar
install -p -m 644 lib/jreleaser-mastodon-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-mastodon-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-mattermost-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-mattermost-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-model-api-1.4.0.jar %{_appdir}/lib/jreleaser-model-api-1.4.0.jar
install -p -m 644 lib/jreleaser-model-impl-1.4.0.jar %{_appdir}/lib/jreleaser-model-impl-1.4.0.jar
install -p -m 644 lib/jreleaser-mustache-1.4.0.jar %{_appdir}/lib/jreleaser-mustache-1.4.0.jar
install -p -m 644 lib/jreleaser-nexus2-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-nexus2-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-resource-bundle-1.4.0.jar %{_appdir}/lib/jreleaser-resource-bundle-1.4.0.jar
install -p -m 644 lib/jreleaser-s3-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-s3-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-sdkman-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-sdkman-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-signing-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-signing-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-slack-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-slack-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-smtp-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-smtp-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-ssh-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-ssh-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-teams-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-teams-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-telegram-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-telegram-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-templates-1.4.0.jar %{_appdir}/lib/jreleaser-templates-1.4.0.jar
install -p -m 644 lib/jreleaser-tool-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-tool-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-twitter-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-twitter-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-utils-1.4.0.jar %{_appdir}/lib/jreleaser-utils-1.4.0.jar
install -p -m 644 lib/jreleaser-webhooks-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-webhooks-java-sdk-1.4.0.jar
install -p -m 644 lib/jreleaser-zulip-java-sdk-1.4.0.jar %{_appdir}/lib/jreleaser-zulip-java-sdk-1.4.0.jar
install -p -m 644 lib/jsonschema-generator-4.28.0.jar %{_appdir}/lib/jsonschema-generator-4.28.0.jar
install -p -m 644 lib/jsonschema-module-jackson-4.28.0.jar %{_appdir}/lib/jsonschema-module-jackson-4.28.0.jar
install -p -m 644 lib/jzlib-1.1.3.jar %{_appdir}/lib/jzlib-1.1.3.jar
install -p -m 644 lib/org.eclipse.jgit-5.13.0.202109080827-r.jar %{_appdir}/lib/org.eclipse.jgit-5.13.0.202109080827-r.jar
install -p -m 644 lib/org.tukaani.xz-0.3.jar %{_appdir}/lib/org.tukaani.xz-0.3.jar
install -p -m 644 lib/os-maven-plugin-1.7.1.jar %{_appdir}/lib/os-maven-plugin-1.7.1.jar
install -p -m 644 lib/picocli-4.7.0.jar %{_appdir}/lib/picocli-4.7.0.jar
install -p -m 644 lib/slf4j-api-2.0.6.jar %{_appdir}/lib/slf4j-api-2.0.6.jar
install -p -m 644 lib/slf4j-simple-2.0.6.jar %{_appdir}/lib/slf4j-simple-2.0.6.jar
install -p -m 644 lib/snakeyaml-1.30.jar %{_appdir}/lib/snakeyaml-1.30.jar
install -p -m 644 lib/sshj-0.34.0.jar %{_appdir}/lib/sshj-0.34.0.jar
install -p -m 644 lib/stax2-api-4.2.1.jar %{_appdir}/lib/stax2-api-4.2.1.jar
install -p -m 644 lib/tika-core-2.6.0.jar %{_appdir}/lib/tika-core-2.6.0.jar
install -p -m 644 lib/twitter4j-core-4.0.7.jar %{_appdir}/lib/twitter4j-core-4.0.7.jar
install -p -m 644 lib/woodstox-core-6.4.0.jar %{_appdir}/lib/woodstox-core-6.4.0.jar
install -p -m 644 lib/yamllint-1.5.0.jar %{_appdir}/lib/yamllint-1.5.0.jar
install -p -m 644 lib/zstd-jni-1.5.2-5.jar %{_appdir}/lib/zstd-jni-1.5.2-5.jar
install -p -m 644 lib/zt-exec-1.12.jar %{_appdir}/lib/zt-exec-1.12.jar

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/bin/jreleaser
%{_datadir}/%{name}/VERSION
%{_datadir}/%{name}/lib/JavaEWAH-1.1.12.jar
%{_datadir}/%{name}/lib/asn-one-0.6.0.jar
%{_datadir}/%{name}/lib/aws-java-sdk-core-1.12.326.jar
%{_datadir}/%{name}/lib/aws-java-sdk-kms-1.12.326.jar
%{_datadir}/%{name}/lib/aws-java-sdk-s3-1.12.326.jar
%{_datadir}/%{name}/lib/bcpg-jdk15on-1.69.jar
%{_datadir}/%{name}/lib/bcpkix-jdk15on-1.69.jar
%{_datadir}/%{name}/lib/bcprov-jdk15on-1.69.jar
%{_datadir}/%{name}/lib/bcutil-jdk15on-1.69.jar
%{_datadir}/%{name}/lib/classmate-1.5.1.jar
%{_datadir}/%{name}/lib/commonmark-0.21.0.jar
%{_datadir}/%{name}/lib/commons-codec-1.15.jar
%{_datadir}/%{name}/lib/commons-compress-1.21.jar
%{_datadir}/%{name}/lib/commons-io-2.11.0.jar
%{_datadir}/%{name}/lib/commons-lang3-3.12.0.jar
%{_datadir}/%{name}/lib/commons-net-3.8.0.jar
%{_datadir}/%{name}/lib/commons-text-1.10.0.jar
%{_datadir}/%{name}/lib/compiler-0.9.10.jar
%{_datadir}/%{name}/lib/eddsa-0.3.0.jar
%{_datadir}/%{name}/lib/failsafe-2.4.4.jar
%{_datadir}/%{name}/lib/feign-core-12.1.jar
%{_datadir}/%{name}/lib/feign-form-3.8.0.jar
%{_datadir}/%{name}/lib/feign-httpclient-12.1.jar
%{_datadir}/%{name}/lib/feign-jackson-12.1.jar
%{_datadir}/%{name}/lib/github-api-1.129.jar
%{_datadir}/%{name}/lib/httpclient-4.5.13.jar
%{_datadir}/%{name}/lib/httpcore-4.4.13.jar
%{_datadir}/%{name}/lib/ion-java-1.0.2.jar
%{_datadir}/%{name}/lib/jackson-annotations-2.14.1.jar
%{_datadir}/%{name}/lib/jackson-core-2.14.1.jar
%{_datadir}/%{name}/lib/jackson-databind-2.14.1.jar
%{_datadir}/%{name}/lib/jackson-dataformat-cbor-2.14.1.jar
%{_datadir}/%{name}/lib/jackson-dataformat-toml-2.14.1.jar
%{_datadir}/%{name}/lib/jackson-dataformat-xml-2.14.1.jar
%{_datadir}/%{name}/lib/jackson-dataformat-yaml-2.14.1.jar
%{_datadir}/%{name}/lib/jakarta.activation-2.0.1.jar
%{_datadir}/%{name}/lib/jakarta.mail-2.0.1.jar
%{_datadir}/%{name}/lib/jcl-over-slf4j-2.0.6.jar
%{_datadir}/%{name}/lib/jmespath-java-1.12.326.jar
%{_datadir}/%{name}/lib/joda-time-2.8.1.jar
%{_datadir}/%{name}/lib/jreleaser-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-artifactory-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-codeberg-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-command-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-config-json-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-config-toml-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-config-yaml-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-discord-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-discourse-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-engine-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-ftp-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-genericgit-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-git-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-gitea-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-github-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-gitlab-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-gitter-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-google-chat-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-graalvm-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-http-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-java-sdk-commons-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-logger-api-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-mastodon-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-mattermost-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-model-api-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-model-impl-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-mustache-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-nexus2-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-resource-bundle-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-s3-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-sdkman-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-signing-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-slack-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-smtp-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-ssh-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-teams-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-telegram-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-templates-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-tool-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-twitter-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-utils-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-webhooks-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jreleaser-zulip-java-sdk-1.4.0.jar
%{_datadir}/%{name}/lib/jsonschema-generator-4.28.0.jar
%{_datadir}/%{name}/lib/jsonschema-module-jackson-4.28.0.jar
%{_datadir}/%{name}/lib/jzlib-1.1.3.jar
%{_datadir}/%{name}/lib/org.eclipse.jgit-5.13.0.202109080827-r.jar
%{_datadir}/%{name}/lib/org.tukaani.xz-0.3.jar
%{_datadir}/%{name}/lib/os-maven-plugin-1.7.1.jar
%{_datadir}/%{name}/lib/picocli-4.7.0.jar
%{_datadir}/%{name}/lib/slf4j-api-2.0.6.jar
%{_datadir}/%{name}/lib/slf4j-simple-2.0.6.jar
%{_datadir}/%{name}/lib/snakeyaml-1.30.jar
%{_datadir}/%{name}/lib/sshj-0.34.0.jar
%{_datadir}/%{name}/lib/stax2-api-4.2.1.jar
%{_datadir}/%{name}/lib/tika-core-2.6.0.jar
%{_datadir}/%{name}/lib/twitter4j-core-4.0.7.jar
%{_datadir}/%{name}/lib/woodstox-core-6.4.0.jar
%{_datadir}/%{name}/lib/yamllint-1.5.0.jar
%{_datadir}/%{name}/lib/zstd-jni-1.5.2-5.jar
%{_datadir}/%{name}/lib/zt-exec-1.12.jar
