# Generated with JReleaser 1.6.0-SNAPSHOT at 2023-04-29T10:13:03.544759325Z
Name:      jreleaser
Version:   1.6.0
Release:   1%{?dist}
Summary:   Release projects quickly and easily with JReleaser

License:   Apache-2.0
URL:       https://jreleaser.org
Source0:   https://github.com/jreleaser/jreleaser/releases/download/v1.6.0/jreleaser-1.6.0.tar

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
%setup -q -n 

%install
mkdir -p %{buildroot}%{_bindir}
%define _appdir %{buildroot}%{_datadir}/%{name}
mkdir -p %{_appdir}/bin

cat > %{buildroot}%{_bindir}/jreleaser <<-EOF
#!/bin/sh
%{_datadir}/%{name}/bin/jreleaser "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/jreleaser

mkdir -p %{_appdir}/releaser-1.6.0
install -p -m 755 releaser-1.6.0/bin/jreleaser %{_appdir}/releaser-1.6.0/bin/jreleaser
install -p -m 644 releaser-1.6.0/LICENSE %{_appdir}/releaser-1.6.0/LICENSE
install -p -m 644 releaser-1.6.0/NOTICE %{_appdir}/releaser-1.6.0/NOTICE
install -p -m 644 releaser-1.6.0/VERSION %{_appdir}/releaser-1.6.0/VERSION
install -p -m 644 releaser-1.6.0/lib/JavaEWAH-1.2.3.jar %{_appdir}/releaser-1.6.0/lib/JavaEWAH-1.2.3.jar
install -p -m 644 releaser-1.6.0/lib/annotations-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/annotations-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/apache-client-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/apache-client-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/arns-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/arns-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/asn-one-0.6.0.jar %{_appdir}/releaser-1.6.0/lib/asn-one-0.6.0.jar
install -p -m 644 releaser-1.6.0/lib/auth-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/auth-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/aws-core-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/aws-core-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/aws-query-protocol-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/aws-query-protocol-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/aws-xml-protocol-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/aws-xml-protocol-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/bcpg-jdk15on-1.70.jar %{_appdir}/releaser-1.6.0/lib/bcpg-jdk15on-1.70.jar
install -p -m 644 releaser-1.6.0/lib/bcpkix-jdk15on-1.70.jar %{_appdir}/releaser-1.6.0/lib/bcpkix-jdk15on-1.70.jar
install -p -m 644 releaser-1.6.0/lib/bcprov-jdk15on-1.70.jar %{_appdir}/releaser-1.6.0/lib/bcprov-jdk15on-1.70.jar
install -p -m 644 releaser-1.6.0/lib/bcutil-jdk15on-1.70.jar %{_appdir}/releaser-1.6.0/lib/bcutil-jdk15on-1.70.jar
install -p -m 644 releaser-1.6.0/lib/classmate-1.5.1.jar %{_appdir}/releaser-1.6.0/lib/classmate-1.5.1.jar
install -p -m 644 releaser-1.6.0/lib/commonmark-0.21.0.jar %{_appdir}/releaser-1.6.0/lib/commonmark-0.21.0.jar
install -p -m 644 releaser-1.6.0/lib/commons-codec-1.15.jar %{_appdir}/releaser-1.6.0/lib/commons-codec-1.15.jar
install -p -m 644 releaser-1.6.0/lib/commons-compress-1.22.jar %{_appdir}/releaser-1.6.0/lib/commons-compress-1.22.jar
install -p -m 644 releaser-1.6.0/lib/commons-io-2.11.0.jar %{_appdir}/releaser-1.6.0/lib/commons-io-2.11.0.jar
install -p -m 644 releaser-1.6.0/lib/commons-jexl3-3.3.jar %{_appdir}/releaser-1.6.0/lib/commons-jexl3-3.3.jar
install -p -m 644 releaser-1.6.0/lib/commons-lang3-3.12.0.jar %{_appdir}/releaser-1.6.0/lib/commons-lang3-3.12.0.jar
install -p -m 644 releaser-1.6.0/lib/commons-net-3.9.0.jar %{_appdir}/releaser-1.6.0/lib/commons-net-3.9.0.jar
install -p -m 644 releaser-1.6.0/lib/commons-text-1.10.0.jar %{_appdir}/releaser-1.6.0/lib/commons-text-1.10.0.jar
install -p -m 644 releaser-1.6.0/lib/compiler-0.9.10.jar %{_appdir}/releaser-1.6.0/lib/compiler-0.9.10.jar
install -p -m 644 releaser-1.6.0/lib/crt-core-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/crt-core-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/eddsa-0.3.0.jar %{_appdir}/releaser-1.6.0/lib/eddsa-0.3.0.jar
install -p -m 644 releaser-1.6.0/lib/endpoints-spi-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/endpoints-spi-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/eventstream-1.0.1.jar %{_appdir}/releaser-1.6.0/lib/eventstream-1.0.1.jar
install -p -m 644 releaser-1.6.0/lib/failsafe-3.3.1.jar %{_appdir}/releaser-1.6.0/lib/failsafe-3.3.1.jar
install -p -m 644 releaser-1.6.0/lib/feign-core-12.3.jar %{_appdir}/releaser-1.6.0/lib/feign-core-12.3.jar
install -p -m 644 releaser-1.6.0/lib/feign-form-3.8.0.jar %{_appdir}/releaser-1.6.0/lib/feign-form-3.8.0.jar
install -p -m 644 releaser-1.6.0/lib/feign-httpclient-12.3.jar %{_appdir}/releaser-1.6.0/lib/feign-httpclient-12.3.jar
install -p -m 644 releaser-1.6.0/lib/feign-jackson-12.3.jar %{_appdir}/releaser-1.6.0/lib/feign-jackson-12.3.jar
install -p -m 644 releaser-1.6.0/lib/http-client-spi-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/http-client-spi-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/httpclient-4.5.13.jar %{_appdir}/releaser-1.6.0/lib/httpclient-4.5.13.jar
install -p -m 644 releaser-1.6.0/lib/httpcore-4.4.16.jar %{_appdir}/releaser-1.6.0/lib/httpcore-4.4.16.jar
install -p -m 644 releaser-1.6.0/lib/jackson-annotations-2.14.2.jar %{_appdir}/releaser-1.6.0/lib/jackson-annotations-2.14.2.jar
install -p -m 644 releaser-1.6.0/lib/jackson-core-2.14.2.jar %{_appdir}/releaser-1.6.0/lib/jackson-core-2.14.2.jar
install -p -m 644 releaser-1.6.0/lib/jackson-databind-2.14.2.jar %{_appdir}/releaser-1.6.0/lib/jackson-databind-2.14.2.jar
install -p -m 644 releaser-1.6.0/lib/jackson-dataformat-toml-2.14.2.jar %{_appdir}/releaser-1.6.0/lib/jackson-dataformat-toml-2.14.2.jar
install -p -m 644 releaser-1.6.0/lib/jackson-dataformat-xml-2.14.2.jar %{_appdir}/releaser-1.6.0/lib/jackson-dataformat-xml-2.14.2.jar
install -p -m 644 releaser-1.6.0/lib/jackson-dataformat-yaml-2.14.2.jar %{_appdir}/releaser-1.6.0/lib/jackson-dataformat-yaml-2.14.2.jar
install -p -m 644 releaser-1.6.0/lib/jakarta.activation-2.0.1.jar %{_appdir}/releaser-1.6.0/lib/jakarta.activation-2.0.1.jar
install -p -m 644 releaser-1.6.0/lib/jakarta.mail-2.0.1.jar %{_appdir}/releaser-1.6.0/lib/jakarta.mail-2.0.1.jar
install -p -m 644 releaser-1.6.0/lib/jcl-over-slf4j-2.0.7.jar %{_appdir}/releaser-1.6.0/lib/jcl-over-slf4j-2.0.7.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-artifactory-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-artifactory-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-azure-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-azure-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-codeberg-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-codeberg-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-command-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-command-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-config-json-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-config-json-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-config-toml-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-config-toml-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-config-yaml-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-config-yaml-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-discord-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-discord-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-discourse-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-discourse-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-engine-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-engine-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-ftp-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-ftp-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-genericgit-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-genericgit-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-git-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-git-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-gitea-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-gitea-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-github-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-github-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-gitlab-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-gitlab-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-gitter-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-gitter-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-google-chat-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-google-chat-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-http-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-http-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-java-sdk-commons-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-java-sdk-commons-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-linkedin-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-linkedin-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-logger-api-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-logger-api-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-mastodon-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-mastodon-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-mattermost-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-mattermost-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-model-api-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-model-api-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-model-impl-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-model-impl-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-nexus2-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-nexus2-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-opencollective-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-opencollective-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-resource-bundle-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-resource-bundle-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-s3-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-s3-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-sdkman-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-sdkman-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-signing-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-signing-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-slack-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-slack-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-smtp-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-smtp-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-ssh-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-ssh-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-teams-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-teams-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-telegram-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-telegram-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-templates-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-templates-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-tool-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-tool-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-twitter-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-twitter-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-utils-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-utils-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-webhooks-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-webhooks-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/jreleaser-zulip-java-sdk-1.6.0.jar %{_appdir}/releaser-1.6.0/lib/jreleaser-zulip-java-sdk-1.6.0.jar
install -p -m 644 releaser-1.6.0/lib/json-utils-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/json-utils-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/jsonschema-generator-4.31.0.jar %{_appdir}/releaser-1.6.0/lib/jsonschema-generator-4.31.0.jar
install -p -m 644 releaser-1.6.0/lib/jsonschema-module-jackson-4.31.0.jar %{_appdir}/releaser-1.6.0/lib/jsonschema-module-jackson-4.31.0.jar
install -p -m 644 releaser-1.6.0/lib/jzlib-1.1.3.jar %{_appdir}/releaser-1.6.0/lib/jzlib-1.1.3.jar
install -p -m 644 releaser-1.6.0/lib/metrics-spi-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/metrics-spi-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/org.eclipse.jgit-5.13.0.202109080827-r.jar %{_appdir}/releaser-1.6.0/lib/org.eclipse.jgit-5.13.0.202109080827-r.jar
install -p -m 644 releaser-1.6.0/lib/picocli-4.7.3.jar %{_appdir}/releaser-1.6.0/lib/picocli-4.7.3.jar
install -p -m 644 releaser-1.6.0/lib/profiles-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/profiles-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/protocol-core-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/protocol-core-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/reactive-streams-1.0.3.jar %{_appdir}/releaser-1.6.0/lib/reactive-streams-1.0.3.jar
install -p -m 644 releaser-1.6.0/lib/regions-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/regions-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/s3-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/s3-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/sdk-core-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/sdk-core-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/slf4j-api-2.0.7.jar %{_appdir}/releaser-1.6.0/lib/slf4j-api-2.0.7.jar
install -p -m 644 releaser-1.6.0/lib/slf4j-simple-2.0.7.jar %{_appdir}/releaser-1.6.0/lib/slf4j-simple-2.0.7.jar
install -p -m 644 releaser-1.6.0/lib/snakeyaml-1.33.jar %{_appdir}/releaser-1.6.0/lib/snakeyaml-1.33.jar
install -p -m 644 releaser-1.6.0/lib/sshj-0.35.0.jar %{_appdir}/releaser-1.6.0/lib/sshj-0.35.0.jar
install -p -m 644 releaser-1.6.0/lib/stax2-api-4.2.1.jar %{_appdir}/releaser-1.6.0/lib/stax2-api-4.2.1.jar
install -p -m 644 releaser-1.6.0/lib/third-party-jackson-core-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/third-party-jackson-core-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/tika-core-2.7.0.jar %{_appdir}/releaser-1.6.0/lib/tika-core-2.7.0.jar
install -p -m 644 releaser-1.6.0/lib/twitter4j-core-4.1.2.jar %{_appdir}/releaser-1.6.0/lib/twitter4j-core-4.1.2.jar
install -p -m 644 releaser-1.6.0/lib/utils-2.20.51.jar %{_appdir}/releaser-1.6.0/lib/utils-2.20.51.jar
install -p -m 644 releaser-1.6.0/lib/woodstox-core-6.5.0.jar %{_appdir}/releaser-1.6.0/lib/woodstox-core-6.5.0.jar
install -p -m 644 releaser-1.6.0/lib/xz-1.9.jar %{_appdir}/releaser-1.6.0/lib/xz-1.9.jar
install -p -m 644 releaser-1.6.0/lib/yamllint-1.5.0.jar %{_appdir}/releaser-1.6.0/lib/yamllint-1.5.0.jar
install -p -m 644 releaser-1.6.0/lib/zstd-jni-1.5.4-1.jar %{_appdir}/releaser-1.6.0/lib/zstd-jni-1.5.4-1.jar
install -p -m 644 releaser-1.6.0/licenses/LICENSE-BSD-2-Clause %{_appdir}/releaser-1.6.0/licenses/LICENSE-BSD-2-Clause
install -p -m 644 releaser-1.6.0/licenses/LICENSE-BSD-2-Clause-FreeBSD %{_appdir}/releaser-1.6.0/licenses/LICENSE-BSD-2-Clause-FreeBSD
install -p -m 644 releaser-1.6.0/licenses/LICENSE-Bouncy-Castle %{_appdir}/releaser-1.6.0/licenses/LICENSE-Bouncy-Castle
install -p -m 644 releaser-1.6.0/licenses/LICENSE-CC0 %{_appdir}/releaser-1.6.0/licenses/LICENSE-CC0
install -p -m 644 releaser-1.6.0/licenses/LICENSE-EDL-1.0 %{_appdir}/releaser-1.6.0/licenses/LICENSE-EDL-1.0
install -p -m 644 releaser-1.6.0/licenses/LICENSE-MIT %{_appdir}/releaser-1.6.0/licenses/LICENSE-MIT
install -p -m 644 releaser-1.6.0/licenses/LICENSE-jzlib %{_appdir}/releaser-1.6.0/licenses/LICENSE-jzlib

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/releaser-1.6.0/bin/jreleaser
%{_datadir}/%{name}/releaser-1.6.0/LICENSE
%{_datadir}/%{name}/releaser-1.6.0/NOTICE
%{_datadir}/%{name}/releaser-1.6.0/VERSION
%{_datadir}/%{name}/releaser-1.6.0/lib/JavaEWAH-1.2.3.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/annotations-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/apache-client-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/arns-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/asn-one-0.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/auth-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/aws-core-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/aws-query-protocol-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/aws-xml-protocol-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/bcpg-jdk15on-1.70.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/bcpkix-jdk15on-1.70.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/bcprov-jdk15on-1.70.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/bcutil-jdk15on-1.70.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/classmate-1.5.1.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/commonmark-0.21.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/commons-codec-1.15.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/commons-compress-1.22.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/commons-io-2.11.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/commons-jexl3-3.3.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/commons-lang3-3.12.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/commons-net-3.9.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/commons-text-1.10.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/compiler-0.9.10.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/crt-core-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/eddsa-0.3.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/endpoints-spi-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/eventstream-1.0.1.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/failsafe-3.3.1.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/feign-core-12.3.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/feign-form-3.8.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/feign-httpclient-12.3.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/feign-jackson-12.3.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/http-client-spi-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/httpclient-4.5.13.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/httpcore-4.4.16.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jackson-annotations-2.14.2.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jackson-core-2.14.2.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jackson-databind-2.14.2.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jackson-dataformat-toml-2.14.2.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jackson-dataformat-xml-2.14.2.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jackson-dataformat-yaml-2.14.2.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jakarta.activation-2.0.1.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jakarta.mail-2.0.1.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jcl-over-slf4j-2.0.7.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-artifactory-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-azure-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-codeberg-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-command-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-config-json-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-config-toml-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-config-yaml-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-discord-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-discourse-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-engine-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-ftp-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-genericgit-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-git-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-gitea-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-github-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-gitlab-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-gitter-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-google-chat-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-http-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-java-sdk-commons-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-linkedin-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-logger-api-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-mastodon-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-mattermost-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-model-api-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-model-impl-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-nexus2-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-opencollective-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-resource-bundle-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-s3-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-sdkman-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-signing-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-slack-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-smtp-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-ssh-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-teams-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-telegram-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-templates-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-tool-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-twitter-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-utils-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-webhooks-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jreleaser-zulip-java-sdk-1.6.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/json-utils-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jsonschema-generator-4.31.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jsonschema-module-jackson-4.31.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/jzlib-1.1.3.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/metrics-spi-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/org.eclipse.jgit-5.13.0.202109080827-r.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/picocli-4.7.3.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/profiles-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/protocol-core-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/reactive-streams-1.0.3.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/regions-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/s3-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/sdk-core-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/slf4j-api-2.0.7.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/slf4j-simple-2.0.7.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/snakeyaml-1.33.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/sshj-0.35.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/stax2-api-4.2.1.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/third-party-jackson-core-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/tika-core-2.7.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/twitter4j-core-4.1.2.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/utils-2.20.51.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/woodstox-core-6.5.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/xz-1.9.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/yamllint-1.5.0.jar
%{_datadir}/%{name}/releaser-1.6.0/lib/zstd-jni-1.5.4-1.jar
%{_datadir}/%{name}/releaser-1.6.0/licenses/LICENSE-BSD-2-Clause
%{_datadir}/%{name}/releaser-1.6.0/licenses/LICENSE-BSD-2-Clause-FreeBSD
%{_datadir}/%{name}/releaser-1.6.0/licenses/LICENSE-Bouncy-Castle
%{_datadir}/%{name}/releaser-1.6.0/licenses/LICENSE-CC0
%{_datadir}/%{name}/releaser-1.6.0/licenses/LICENSE-EDL-1.0
%{_datadir}/%{name}/releaser-1.6.0/licenses/LICENSE-MIT
%{_datadir}/%{name}/releaser-1.6.0/licenses/LICENSE-jzlib
