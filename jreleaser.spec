Name:       jreleaser
Version:    0.9.0
Release:    1%{?dist}
Summary:    Release projects quickly and easily with JReleaser 

License:    Apache-2.0
URL:        https://github.com/jreleaser/%{name}
Source0:    https://github.com/jreleaser/%{name}/releases/download/v%{version}/%{name}-%{version}.tar

BuildArch:      noarch
BuildRequires:  git
Requires:       java

%description
JReleaser is a release automation tool for Java projects. Its goal is to simplify creating releases
and publishing artifacts to multiple package managers while providing customizable options.

JReleaser takes inputs from popular builds tools (Ant, Maven, Gradle) such as JAR files, binary
distributions (.zip, .tar), JLink images, or any other file that you’d like to publish as a Git
release on popular Git services such as Github or Gitlab. Distribution files can additionally be
published to be consumed by popular package managers as Homebrew, Snapcraft, or get ready to be
launched via JBang. Releases may be announced in a variety of channels such as Twitter, Zulip, or SDKMAN!

%prep
%autosetup -S git


%install
mkdir -p %{buildroot}%{_bindir}
# launcher script expects all JARs to reside at ../lib
# %{_lib} may resolve to "lib64" thus we force the use of "lib"
%define lib_dir %{buildroot}%{_bindir}/../lib
mkdir -p %{lib_dir}
install -p -m 755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -p -m 644 lib/JavaEWAH-1.1.12.jar %{lib_dir}/JavaEWAH-1.1.12.jar
install -p -m 644 lib/artifactory-java-sdk-0.9.0.jar %{lib_dir}/artifactory-java-sdk-0.9.0.jar
install -p -m 644 lib/aws-java-sdk-core-1.12.118.jar %{lib_dir}/aws-java-sdk-core-1.12.118.jar
install -p -m 644 lib/aws-java-sdk-kms-1.12.118.jar %{lib_dir}/aws-java-sdk-kms-1.12.118.jar
install -p -m 644 lib/aws-java-sdk-s3-1.12.118.jar %{lib_dir}/aws-java-sdk-s3-1.12.118.jar
install -p -m 644 lib/bcpg-jdk15on-1.68.jar %{lib_dir}/bcpg-jdk15on-1.68.jar
install -p -m 644 lib/bcprov-jdk15on-1.68.jar %{lib_dir}/bcprov-jdk15on-1.68.jar
install -p -m 644 lib/codeberg-java-sdk-0.9.0.jar %{lib_dir}/codeberg-java-sdk-0.9.0.jar
install -p -m 644 lib/commons-codec-1.15.jar %{lib_dir}/commons-codec-1.15.jar
install -p -m 644 lib/commons-compress-1.21.jar %{lib_dir}/commons-compress-1.21.jar
install -p -m 644 lib/commons-io-2.11.0.jar %{lib_dir}/commons-io-2.11.0.jar
install -p -m 644 lib/commons-lang3-3.12.0.jar %{lib_dir}/commons-lang3-3.12.0.jar
install -p -m 644 lib/compiler-0.9.10.jar %{lib_dir}/compiler-0.9.10.jar
install -p -m 644 lib/discord-java-sdk-0.9.0.jar %{lib_dir}/discord-java-sdk-0.9.0.jar
install -p -m 644 lib/feign-core-11.7.jar %{lib_dir}/feign-core-11.7.jar
install -p -m 644 lib/feign-form-3.8.0.jar %{lib_dir}/feign-form-3.8.0.jar
install -p -m 644 lib/feign-httpclient-11.7.jar %{lib_dir}/feign-httpclient-11.7.jar
install -p -m 644 lib/feign-jackson-11.7.jar %{lib_dir}/feign-jackson-11.7.jar
install -p -m 644 lib/genericgit-java-sdk-0.9.0.jar %{lib_dir}/genericgit-java-sdk-0.9.0.jar
install -p -m 644 lib/git-sdk-0.9.0.jar %{lib_dir}/git-sdk-0.9.0.jar
install -p -m 644 lib/gitea-java-sdk-0.9.0.jar %{lib_dir}/gitea-java-sdk-0.9.0.jar
install -p -m 644 lib/github-api-1.129.jar %{lib_dir}/github-api-1.129.jar
install -p -m 644 lib/github-java-sdk-0.9.0.jar %{lib_dir}/github-java-sdk-0.9.0.jar
install -p -m 644 lib/gitlab-java-sdk-0.9.0.jar %{lib_dir}/gitlab-java-sdk-0.9.0.jar
install -p -m 644 lib/gitter-java-sdk-0.9.0.jar %{lib_dir}/gitter-java-sdk-0.9.0.jar
install -p -m 644 lib/google-chat-java-sdk-0.9.0.jar %{lib_dir}/google-chat-java-sdk-0.9.0.jar
install -p -m 644 lib/http-upload-java-sdk-0.9.0.jar %{lib_dir}/http-upload-java-sdk-0.9.0.jar
install -p -m 644 lib/httpclient-4.5.13.jar %{lib_dir}/httpclient-4.5.13.jar
install -p -m 644 lib/httpcore-4.4.13.jar %{lib_dir}/httpcore-4.4.13.jar
install -p -m 644 lib/ion-java-1.0.2.jar %{lib_dir}/ion-java-1.0.2.jar
install -p -m 644 lib/jackson-annotations-2.13.0.jar %{lib_dir}/jackson-annotations-2.13.0.jar
install -p -m 644 lib/jackson-core-2.13.0.jar %{lib_dir}/jackson-core-2.13.0.jar
install -p -m 644 lib/jackson-databind-2.13.0.jar %{lib_dir}/jackson-databind-2.13.0.jar
install -p -m 644 lib/jackson-dataformat-cbor-2.13.0.jar %{lib_dir}/jackson-dataformat-cbor-2.13.0.jar
install -p -m 644 lib/jackson-dataformat-toml-2.13.0.jar %{lib_dir}/jackson-dataformat-toml-2.13.0.jar
install -p -m 644 lib/jackson-dataformat-yaml-2.13.0.jar %{lib_dir}/jackson-dataformat-yaml-2.13.0.jar
install -p -m 644 lib/jakarta.activation-2.0.1.jar %{lib_dir}/jakarta.activation-2.0.1.jar
install -p -m 644 lib/jakarta.mail-2.0.1.jar %{lib_dir}/jakarta.mail-2.0.1.jar
install -p -m 644 lib/java-sdk-commons-0.9.0.jar %{lib_dir}/java-sdk-commons-0.9.0.jar
install -p -m 644 lib/javassist-3.26.0-GA.jar %{lib_dir}/javassist-3.26.0-GA.jar
install -p -m 644 lib/jcl-over-slf4j-1.7.32.jar %{lib_dir}/jcl-over-slf4j-1.7.32.jar
install -p -m 644 lib/jmespath-java-1.12.118.jar %{lib_dir}/jmespath-java-1.12.118.jar
install -p -m 644 lib/joda-time-2.8.1.jar %{lib_dir}/joda-time-2.8.1.jar
install -p -m 644 lib/jreleaser-0.9.0.jar %{lib_dir}/jreleaser-0.9.0.jar
install -p -m 644 lib/jreleaser-assemblers-0.9.0.jar %{lib_dir}/jreleaser-assemblers-0.9.0.jar
install -p -m 644 lib/jreleaser-config-json-0.9.0.jar %{lib_dir}/jreleaser-config-json-0.9.0.jar
install -p -m 644 lib/jreleaser-config-toml-0.9.0.jar %{lib_dir}/jreleaser-config-toml-0.9.0.jar
install -p -m 644 lib/jreleaser-config-yaml-0.9.0.jar %{lib_dir}/jreleaser-config-yaml-0.9.0.jar
install -p -m 644 lib/jreleaser-engine-0.9.0.jar %{lib_dir}/jreleaser-engine-0.9.0.jar
install -p -m 644 lib/jreleaser-model-0.9.0.jar %{lib_dir}/jreleaser-model-0.9.0.jar
install -p -m 644 lib/jreleaser-templates-0.9.0.jar %{lib_dir}/jreleaser-templates-0.9.0.jar
install -p -m 644 lib/jreleaser-tools-0.9.0.jar %{lib_dir}/jreleaser-tools-0.9.0.jar
install -p -m 644 lib/jreleaser-utils-0.9.0.jar %{lib_dir}/jreleaser-utils-0.9.0.jar
install -p -m 644 lib/jreleaser-workflow-0.9.0.jar %{lib_dir}/jreleaser-workflow-0.9.0.jar
install -p -m 644 lib/mail-java-sdk-0.9.0.jar %{lib_dir}/mail-java-sdk-0.9.0.jar
install -p -m 644 lib/mastodon-java-sdk-0.9.0.jar %{lib_dir}/mastodon-java-sdk-0.9.0.jar
install -p -m 644 lib/mattermost-java-sdk-0.9.0.jar %{lib_dir}/mattermost-java-sdk-0.9.0.jar
install -p -m 644 lib/org.eclipse.jgit-5.13.0.202109080827-r.jar %{lib_dir}/org.eclipse.jgit-5.13.0.202109080827-r.jar
install -p -m 644 lib/os-maven-plugin-1.7.0.jar %{lib_dir}/os-maven-plugin-1.7.0.jar
install -p -m 644 lib/picocli-4.6.2.jar %{lib_dir}/picocli-4.6.2.jar
install -p -m 644 lib/reflections-0.9.12.jar %{lib_dir}/reflections-0.9.12.jar
install -p -m 644 lib/s3-java-sdk-0.9.0.jar %{lib_dir}/s3-java-sdk-0.9.0.jar
install -p -m 644 lib/sdkman-java-sdk-0.9.0.jar %{lib_dir}/sdkman-java-sdk-0.9.0.jar
install -p -m 644 lib/slack-java-sdk-0.9.0.jar %{lib_dir}/slack-java-sdk-0.9.0.jar
install -p -m 644 lib/slf4j-api-1.7.32.jar %{lib_dir}/slf4j-api-1.7.32.jar
install -p -m 644 lib/slf4j-simple-1.7.32.jar %{lib_dir}/slf4j-simple-1.7.32.jar
install -p -m 644 lib/snakeyaml-1.29.jar %{lib_dir}/snakeyaml-1.29.jar
install -p -m 644 lib/teams-java-sdk-0.9.0.jar %{lib_dir}/teams-java-sdk-0.9.0.jar
install -p -m 644 lib/telegram-java-sdk-0.9.0.jar %{lib_dir}/telegram-java-sdk-0.9.0.jar
install -p -m 644 lib/tika-core-2.1.0.jar %{lib_dir}/tika-core-2.1.0.jar
install -p -m 644 lib/twitter-java-sdk-0.9.0.jar %{lib_dir}/twitter-java-sdk-0.9.0.jar
install -p -m 644 lib/twitter4j-core-4.0.7.jar %{lib_dir}/twitter4j-core-4.0.7.jar
install -p -m 644 lib/webhooks-java-sdk-0.9.0.jar %{lib_dir}/webhooks-java-sdk-0.9.0.jar
install -p -m 644 lib/yamllint-1.4.0.jar %{lib_dir}/yamllint-1.4.0.jar
install -p -m 644 lib/zt-exec-1.12.jar %{lib_dir}/zt-exec-1.12.jar
install -p -m 644 lib/zulip-java-sdk-0.9.0.jar %{lib_dir}/zulip-java-sdk-0.9.0.jar

%files
%{_bindir}/jreleaser
%{_exec_prefix}/lib/JavaEWAH-1.1.12.jar
%{_exec_prefix}/lib/artifactory-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/aws-java-sdk-core-1.12.118.jar
%{_exec_prefix}/lib/aws-java-sdk-kms-1.12.118.jar
%{_exec_prefix}/lib/aws-java-sdk-s3-1.12.118.jar
%{_exec_prefix}/lib/bcpg-jdk15on-1.68.jar
%{_exec_prefix}/lib/bcprov-jdk15on-1.68.jar
%{_exec_prefix}/lib/codeberg-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/commons-codec-1.15.jar
%{_exec_prefix}/lib/commons-compress-1.21.jar
%{_exec_prefix}/lib/commons-io-2.11.0.jar
%{_exec_prefix}/lib/commons-lang3-3.12.0.jar
%{_exec_prefix}/lib/compiler-0.9.10.jar
%{_exec_prefix}/lib/discord-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/feign-core-11.7.jar
%{_exec_prefix}/lib/feign-form-3.8.0.jar
%{_exec_prefix}/lib/feign-httpclient-11.7.jar
%{_exec_prefix}/lib/feign-jackson-11.7.jar
%{_exec_prefix}/lib/genericgit-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/git-sdk-0.9.0.jar
%{_exec_prefix}/lib/gitea-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/github-api-1.129.jar
%{_exec_prefix}/lib/github-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/gitlab-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/gitter-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/google-chat-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/http-upload-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/httpclient-4.5.13.jar
%{_exec_prefix}/lib/httpcore-4.4.13.jar
%{_exec_prefix}/lib/ion-java-1.0.2.jar
%{_exec_prefix}/lib/jackson-annotations-2.13.0.jar
%{_exec_prefix}/lib/jackson-core-2.13.0.jar
%{_exec_prefix}/lib/jackson-databind-2.13.0.jar
%{_exec_prefix}/lib/jackson-dataformat-cbor-2.13.0.jar
%{_exec_prefix}/lib/jackson-dataformat-toml-2.13.0.jar
%{_exec_prefix}/lib/jackson-dataformat-yaml-2.13.0.jar
%{_exec_prefix}/lib/jakarta.activation-2.0.1.jar
%{_exec_prefix}/lib/jakarta.mail-2.0.1.jar
%{_exec_prefix}/lib/java-sdk-commons-0.9.0.jar
%{_exec_prefix}/lib/javassist-3.26.0-GA.jar
%{_exec_prefix}/lib/jcl-over-slf4j-1.7.32.jar
%{_exec_prefix}/lib/jmespath-java-1.12.118.jar
%{_exec_prefix}/lib/joda-time-2.8.1.jar
%{_exec_prefix}/lib/jreleaser-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-assemblers-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-config-json-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-config-toml-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-config-yaml-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-engine-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-model-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-templates-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-tools-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-utils-0.9.0.jar
%{_exec_prefix}/lib/jreleaser-workflow-0.9.0.jar
%{_exec_prefix}/lib/mail-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/mastodon-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/mattermost-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/org.eclipse.jgit-5.13.0.202109080827-r.jar
%{_exec_prefix}/lib/os-maven-plugin-1.7.0.jar
%{_exec_prefix}/lib/picocli-4.6.2.jar
%{_exec_prefix}/lib/reflections-0.9.12.jar
%{_exec_prefix}/lib/s3-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/sdkman-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/slack-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/slf4j-api-1.7.32.jar
%{_exec_prefix}/lib/slf4j-simple-1.7.32.jar
%{_exec_prefix}/lib/snakeyaml-1.29.jar
%{_exec_prefix}/lib/teams-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/telegram-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/tika-core-2.1.0.jar
%{_exec_prefix}/lib/twitter-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/twitter4j-core-4.0.7.jar
%{_exec_prefix}/lib/webhooks-java-sdk-0.9.0.jar
%{_exec_prefix}/lib/yamllint-1.4.0.jar
%{_exec_prefix}/lib/zt-exec-1.12.jar
%{_exec_prefix}/lib/zulip-java-sdk-0.9.0.jar